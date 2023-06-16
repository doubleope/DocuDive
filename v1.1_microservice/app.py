import os
import flask
from flask import Flask, request
# from werkzeug.middleware.proxy_fix import ProxyFix
import json
import time
from datetime import datetime
import sys
from DocuDive import loadModel, getResult


def model_fn():
    return loadModel()

def predict(body: dict, llm):
    query = body["query"]
    answer, documents = getResult(query, llm)
    result = {
        "answer":answer,
        "Documents":{}
        }
    for doc in documents:
        result['Documents'][doc.metadata["source"]] = doc.page_content

    return result

app = Flask(__name__, static_url_path='', static_folder='web/static')

# Load the model by reading the `SM_MODEL_DIR` environment variable
# which is passed to the container by SageMaker (usually /opt/ml/model).
llm = model_fn()

# Since the web application runs behind a proxy (nginx), we need to
# add this setting to our app.
# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )


@app.route("/keepalive")
def keepalive():
    """
    Healthcheck function.
    """
    return "up"


@app.route("/api/ask", methods=["POST"])
def invocations():
    """
    Function which responds to the invocations requests.
    """
    body = request.json
    if not body.query:
        return "Missing 'query' in POST JSON body"
    isSuccess = True
    result = {}
    try:
        start = time.time()
        result = predict(body, llm)
        end = time.time()
    except:
        isSuccess = False
    

    response = {
        "result" : result,
        "timestamp":datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "isSuccess":isSuccess,
        "jobDurationSeconds": round(end - start, 0)
    }

    responsejson = json.dumps(response, indent=4)
    return flask.Response(response=responsejson, status=200, mimetype='application/json')

if __name__ == "__main__":
    # Using host="localhost" will not connect to the public IP in AWS EC2. You have to use 0.0.0.0
    app.run(host='0.0.0.0',port=8080)
import os
import flask
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

from sagemaker.inference import model_fn, predict
import json


app = Flask(__name__)

# Load the model by reading the `SM_MODEL_DIR` environment variable
# which is passed to the container by SageMaker (usually /opt/ml/model).
llm = model_fn()

# Since the web application runs behind a proxy (nginx), we need to
# add this setting to our app.
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


@app.route("/ping", methods=["GET"])
def ping():
    """
    Healthcheck function.
    """
    return "pong"


@app.route("/invocations", methods=["POST"])
def invocations():
    """
    Function which responds to the invocations requests.
    """
    body = request.json
    result = predict(body, llm)
    resultjson = json.dump(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')
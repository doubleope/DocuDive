import json
import flask
dict = {"hello":"world"}
resultjson = json.dumps(dict, indent=4)
print(flask.Response(response=resultjson, status=200, mimetype='application/json'))
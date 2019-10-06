from sklearn.externals import joblib
import numpy as np
from flask import Flask, jsonify, request
import gunicorn

app = Flask(__name__)

@app.route("/")
def hello():
 return "Hello "

@app.route('/predict', methods=['POST'])
def apicall():
    try:
        test_json = request.get_json()
        val = []
        print(test_json)
        for dic in test_json:
           row = []
           row.append(dic['sepal_length'])
           row.append(dic['sepal_width'])
           row.append(dic['petal_length'])
           row.append(dic['petal_width'])
           val.append(row)
        print(np.array(val))
        loaded_model = joblib.load('model/iris_svm_model.pkl')
        y_pred = loaded_model.predict(np.array(val))
        pred_dict = {}
        for i,pred in enumerate(y_pred):
           pred_dict['prediction_'+str(i)] = int(pred)
        responses = jsonify(predictions=pred_dict)
        responses.status_code = 200
    except Exception as e:
        responses = jsonify(predictions={'error':e})
        responses.status_code = 404
        print ('error', e)
    return (responses)
from flask import Flask,request
import json
import numpy as np

APP =Flask(__name__)

model = joblib.load(r' ')

@APP.route('/predict',methods=['POST'])

def predict():
	event = json.loads(request.data)
	#print(event)
	values = event['values']
	values = list(map(np.float,values))
	pre = np.array(values)
    pre = pre.reshape(1,-1)
    res = model.predict(pre)
    print(res)
	return "1"
	
if __name__ == '__main__':
	APP.run(debug=True)
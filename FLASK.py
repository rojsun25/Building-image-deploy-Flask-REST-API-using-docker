#pip install flask

from flask import Flask,request
import json

APP =Flask(__name__)

@APP.route("/heysimple",methods=['GET'])
def hello():
    req = request.args
    req = req.to_dict()
    return str("Hello "+req['name'])
    
@APP.route('/addpost',methods=['POST'])
def add():
    req=request.data
    req = json.loads(req)
    c = req['First name'] + req['Last name']
    return str(c)

if __name__ == "__main__":
    APP.run(debug=True)
#req1 = hello("Rojsun")




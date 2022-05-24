
from flask import Flask,request
import json

APP =Flask(__name__)

@APP.route('/')
def hello():
    return "hello"


if __name__ == "__main__":
    APP.run(debug=True)
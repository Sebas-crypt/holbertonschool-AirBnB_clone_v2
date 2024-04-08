#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/, strict_slashes = false")
@app.route("/HBNB")

def hello():
    return 'Hello HBNB!'
def hello() :
    return 'HBNB'

if __name__ == '__main__':
    app.run ('host=0.0.0.0', 'port=5000')


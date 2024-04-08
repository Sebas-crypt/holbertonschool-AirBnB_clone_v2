#!/usr/bin/python3
from flask import Flask
app = Flask(__main__)

@app.route("/, strict_slashes = false")

def hello():
    return 'Hello HBNB!'

if name = __main__:
    app.run ('host=0.0.0.0', 'port=5000')

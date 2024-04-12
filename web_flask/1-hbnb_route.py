#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ Returns some text. """
    return 'Hello HBNB!'

@app.route("/HBNB", strict_slashes=False)
def hbnb():
    """ Return other text. """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

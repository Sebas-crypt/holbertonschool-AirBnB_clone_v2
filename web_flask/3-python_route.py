 #!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes =False)
def hello():
    return 'Hello HBNB!'

@app.route("/HBNB", strict_slashes =False)
def hbnb() :
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def text(text):
    text = text.replace ("_", " ")
    return("C {}".format(text))

@app.route ("/python/<text>", strict_slashes=False)
def texts(text):
    text = text.replace("_"," ")
    return("python {}".format(text))

@app.route("/number/<n>", strict_slashes=False)
def numbers(n):
    if n.isdigit():
        return '{} is a number'.format(n)
    
if __name__ == '__main__':
    app.run (host='0.0.0.0', port=5000)
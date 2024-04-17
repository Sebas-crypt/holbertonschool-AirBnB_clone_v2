#!/usr/bin/python3
""" starts the flask app """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/HBNB', strict_slashes=False)
def hbnb():
    """ Returns other text. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Replace text with variable. """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def texts(text):
    """ Replace more text with another variable. """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    """ Replace with int only if given int. """
    return str(n) + " is a number "


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templates(n):
    """ Display html if n is int. """
        return render_template ("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ Display different page depending on var given odd or even. """
    return render_template ("6-number_odd_or_even.html", n=n, Evenodd = Evenodd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

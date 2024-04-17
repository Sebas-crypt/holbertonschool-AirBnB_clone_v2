#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes =False)
def hello():
    """ Returns some text. """
    return 'Hello HBNB!'

@app.route('/HBNB', strict_slashes =False)
def hbnb():
    """ Returns other text. """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Replace text with variable. """
    text = text.replace ("_", " ")
    return("C {}".format(text))

@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def texts(text):
    """ Replace more text with another variable. """
    text = text.replace("_"," ")
    return("python {}".format(text))

@app.route('/number/<n>', strict_slashes=False)
def numbers(n):
    """ Replace with int only if given int. """
    if n.isdigit():
        return '{} is a number'.format(n)

@app.route('/number_template/<n>', strict_slashes=False)
def number_templates(n):
    """ Display html if n is int. """
    if n.isdigit():
        return render_template ('5-number.html', n=n)

@app.route('/number_odd_or_even/', strict_slashes=False)
def odd_or_even(n):
    """ Display different page depending on var given odd or even. """
    if n.isdigit():
        if int(n) %2 == 0:
            Evenodd = "even"
        else:
            if int(n) %5 == 0:
                Evenodd = "odd"
                return render_template ('6-number_odd_or_even.html', n=n, Evenodd = Evenodd)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

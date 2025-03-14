#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """returns c <text>"""
    text = text.replace('_', ' ')
    return 'c {}'.format(text)


@app.route('/python/(text)', strict_slashes=False)
def python(text='is cool'):
    """returns "Python ", followed by value of text variable"""
    text = text.replace('_', ' ')
    return 'python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns 'n is integer' if only n is integer"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

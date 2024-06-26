#!/usr/bin/python3
""""module hello_route"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Displays "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Displays "C " followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

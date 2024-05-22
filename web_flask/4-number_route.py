#!/usr/bin/python3
""""module hello_route"""
from flask import Flask
from str import isnumeric

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


@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """
    Displays "Python " followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    Displays a message indicating whether the input value is a number or not.

    Args:
        n (str): The input value to be checked.

    Returns:
        str: A message indicating whether the input value is a number or not.
    """
    if n.isnumeric():
        return n + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

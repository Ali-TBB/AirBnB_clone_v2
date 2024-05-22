#!/usr/bin/python3
""""module hello_route"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays a message indicating whether the input value is a number or not.

    Args:
        n (int): The input value to be checked.

    Returns:
        str: A message indicating whether the input value is a number or not.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders a template called '5-number_template.html' and
    passes the value of 'n' to it.

    Args:
        n (int): The number to be passed to the template.

    Returns:
        The rendered template with the value of 'n' passed to it.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Renders a template called 'number_odd_or_even.html' and
    passes the value of 'n' and its even/odd status to it.

    Args:
        n (int): The number to be passed to the template.

    Returns:
        The rendered template with the value of 'n' and its even/odd status passed to it.
    """
    if n % 2 == 0:
        status = "even"
    else:
        status = "odd"
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

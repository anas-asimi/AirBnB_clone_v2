#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text: str):
    """returns C text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text: str = 'is cool'):
    """returns Python text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n: str):
    """returns n is a number"""
    try:
        return '{} is a number'.format(int(n))
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n: str):
    """returns <h1>Number: n<h1>"""
    try:
        return render_template('5-number.html', n=int(n))
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

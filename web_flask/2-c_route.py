#!/usr/bin/python3
"""
second route test 2
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    conect to first path '/'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    second path conect second rout '/hbnb'
    """
    return "HBNB"


@app.route('/c/<text>/', strict_slashes=False)
def c(text):
    """
    send a parametter
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()

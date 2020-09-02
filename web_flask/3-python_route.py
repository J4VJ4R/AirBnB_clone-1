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

@app.route('/python/(<text>)/', strict_slashes=False)
def python(text):
    """
    four route recive a text
    """
    if text is null:
        return "Python {}".format(text.replace("_", " "))
    else:
        return "is cool"


if __name__ == "__main__":
    app.run()

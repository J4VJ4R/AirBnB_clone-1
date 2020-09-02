#!/usr/bin/python3
"""
This code is to create a test with Flask
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """
    this functión use slash '/' to show result or return some
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
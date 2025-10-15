"""
External modules are those are written by developers and we can use them by installing them in our system with pip install command
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(debug=True)
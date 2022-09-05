#!/usr/bin/env python3
from flask import Flask, send_from_directory, url_for
import os


app = Flask(__name__)

@app.route('/')
def home():
    return """
<html>
<h1>Flask website playground</h1>
<h3>So far:</h3>
<ul>
<li> added root path
<li> added static folder
<li> added cat favicon
<li> added <a href="/spock">spock</a> route with pixel Spock
<li> added the <a href="/about">about page</a>
</ul> 
... more to come
<html>
"""

@app.route('/about')
def about():
    return """
    This is a little about page, content TBA
    """

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/spock')
def spock():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'spock-pixel.png', mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
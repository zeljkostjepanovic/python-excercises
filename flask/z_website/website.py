#!/usr/bin/env python3
from flask import Flask, send_from_directory, url_for,render_template
import os


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/main.css')
def main_css():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'css/main.css', mimetype='text/css')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/spock')
def spock():
    return render_template("spock.html")

@app.route('/spock-image')
def spock_img():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'spock-pixel.png', mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for, request, redirect
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
	error = request.args.get('error')
    return render_template('site.html', weather=None, error=error)

@app.route('/site')
def site():

from flask import Flask, render_template, url_for, request, redirect
import requests
import os
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	error = request.args.get('error')
	return render_template('index.html', error=error)

@app.route('/get_message', methods=['GET', 'POST'])
def get_message():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']
		message = request.form['message']
		return redirect(url_for('typ'))

	else:
		return redirect(url_for('/'))

@app.route('/typ')
def typ():
	error = request.args.get('error')
	return render_template('typ.html', error=error)


port = int(os.environ.get('POST', 5000))
if __name__ == '__main__':
	app.run(threaded=True, port=port, debug=True)

from flask import Flask, render_template, url_for, request, redirect
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
	error = request.args.get('error')
	return render_template('fixtron.html', error=error)

@app.route('/get_message', methods=['POST'])
def get_message():
	try:
		firstName = request.form['fname']
		lastName = request.form['lname']
		message = request.form['subject']
		if message == '':
			return redirect(url_for('index', error="Please fill out the message portion"))
		else:
			return redirect(url_for('typ'))
	except:
		return redirect(url_for('fixtron'))
	print(message)

port = int(os.environ.get("POST", 5000))
if __name__ == '__main__':
	app.run(threaded=True, port=port)

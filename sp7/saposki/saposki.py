from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g
from functools import wraps



import sqlite3

#config
DATABASE = 'sblog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hardtoguess'

app = Flask(__name__)


#pulls in configurations
app.config.from_object(__name__)


#connecting db 
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def home():
	return render_template('main.html')

@app.route('/portrait')
def portrait():
	return render_template('portrait.html')

@app.route('/lifestyle')
def lifestyle():
	return	render_template('lifestyle.html')

@app.route('/candid')
def candid():
	return	render_template('candid.html')

@app.route('/about')
def about():
	return	render_template('about.html')

@app.route('/contact')
def contact():
	return	render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('listcomments'))
	return	render_template('login.html', error=error)

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@app.route('/list-comments')
@login_required
def listcomments():
	return render_template('list-comments.html')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('login'))


if __name__ == "__main__":
	app.run(debug=True)
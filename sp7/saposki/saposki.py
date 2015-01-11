from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g

import sqlite3

DATABASE = 'sblog.db'

app = Flask(__name__)

#pulls in configurations
app.config.from_object(__name__)

#connecting db 
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route("/home")
def home():
	return render_template('main.html')

@app.route("/portrait")
def portrait():
	return render_template('portrait.html')

@app.route("/lifestyle")
def lifestyle():
	return	render_template('lifestyle.html')

@app.route("/candid")
def candid():
	return	render_template('candid.html')

@app.route("/about")
def about():
	return	render_template('about.html')

@app.route("/contact")
def contact():
	return	render_template('contact.html')

@app.route("/login")
def login():
	return	render_template('login.html')

if __name__ == "__main__":
	app.run(debug=True)
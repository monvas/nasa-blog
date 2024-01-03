from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os

#mysql_host = os.environ.get('MYSQL_HOST','mysql')
mysql_user = os.environ.get('MYSQL_USER')
mysql_pwd = os.environ.get('MYSQL_ROOT_PASSWORD')
mysql_db = os.environ.get('MYSQL_DATABASE')

app = Flask(__name__)

app.secret_key = 'obkasbbindkawida'

app.config['MYSQL_HOST'] = 'mysql' #mysql_host
app.config['MYSQL_USER'] = mysql_user
app.config['MYSQL_PASSWORD'] = mysql_pwd
app.config['MYSQL_DB'] = mysql_db

mysql = MySQL(app)

@app.route('/login', methods =['GET', 'POST'])
def login():
	print("login started")
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password, ))
		account = cursor.fetchone()
		print(account)
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['email'] = account['email']
			msg = 'Logged in successfully !'
			print(msg)
			return redirect('http://0.0.0.0:8080') #return redirect(url_for('home'))
		else:
			msg = 'Incorrect username / password !'
	return render_template('sign-in.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('email', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'password' in request.form and 'email' in request.form :
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE email = % s', (email, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s)', (password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
			return redirect('http://0.0.0.0:5001/login') #(url_for('login')) 
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('sign-up.html', msg = msg)

@app.route('/')
def home():
    return redirect('http://127.0.0.1:8080')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

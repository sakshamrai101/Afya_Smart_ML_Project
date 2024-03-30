from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from app import app
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the file path to data.csv
db_file_path = os.path.join(current_dir, 'data', 'database.db')


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)
from config import Config

app.secret_key = Config.SECRET_KEY
print("secret key:",app.secret_key)

# Route to handle user login
@app.route('/', methods=["GET"])
def index():
    print(1000)
    return render_template('index.html')

@app.route('/PCP_login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    print('user:', user)
    if user:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password', 'error')
        return redirect(url_for('index'))

# Route to handle dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('index'))

# Route to handle logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
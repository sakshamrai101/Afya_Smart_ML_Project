from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from app import app
import os
import sys
from .userstory1 import conversation_loop
from .userstory3 import recommendations_conversation_loop
from .userstory2 import main
from twilio.rest import Client 
from .keys import account_sid, target_number, auth_token, twilio_number



current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the file path to data.csv
db_file_path = os.path.join(current_dir, 'data', 'database.db')


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)
from config import Config

app.secret_key = Config.SECRET_KEY
print("secret key:",app.secret_key)
app.open_ai_key = Config.OPENAI_API_KEY
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
        return redirect(url_for('import_page'))
    else:
        flash('Invalid username or password', 'error')
        return redirect(url_for('index'))

# Route to handle dashboard
@app.route('/home')
def import_page():
    if 'username' in session:
        return render_template('import_page.html', username=session['username'])
    else:
        return redirect(url_for('index'))
    
@app.route('/operation3', methods=['GET','POST'])
def operation3():
    return render_template('operation3.html')

@app.route('/operation2', methods=['GET','POST'])
def operation2():
    return render_template('operation2.html')

# Route to handle logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/operation1', methods=['GET','POST'])
def operation1():
    return render_template('operation1.html')

@app.route('/Missing_info', methods=['POST'])
def missing_info():
    missing_info_list = conversation_loop()
    
    # Convert missing_info_list to a formatted string
    formatted_message = "\n".join([f"{item['number']}. {item['info']}" for item in missing_info_list])

    # Setup for sending notifications to PCP upon generating missing info checklist.
    client = Client(account_sid, auth_token)

    # Send the formatted message as the body of the Twilio message
    message = client.messages.create(
        body=formatted_message,
        from_=twilio_number,
        to=target_number
    )

    return render_template('missing_info.html', missing_info_list=missing_info_list)

@app.route('/Targeted_questions', methods=['POST'])
def targeted_questions():
    targeted_questions_list = main()
    questions_to_display = targeted_questions_list.split('\n') 
    return render_template('targeted_questions.html', questions=questions_to_display)

@app.route('/Recommendations', methods=['POST'])
def recommendations():
    reco = recommendations_conversation_loop()
    reco = '<br>'.join(reco.split('\n'))
    return render_template('recommendations.html', reco=reco)

@app.route('/operation4')
def operation4():
    return render_template('operation4.html')
import mysql.connector
from flask import Blueprint
from flask import Flask,Blueprint, request, jsonify
from flask_cors import CORS

# app = Flask(__name__)
app = Blueprint('login', __name__)
CORS(app)

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='sdp'  # Name of your MySQL database in MySQL Workbench
)
c = conn.cursor()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # Check if the email is already registered
    c.execute("SELECT * FROM users WHERE email=%s", (email,))
    existing_user = c.fetchone()

    if existing_user:
    # if email in registered_users:
        return jsonify({'error': 'Email already registered'}), 400

    # registered_users[email] = {'username': username, 'password': password}
    # Insert the new user details into the database
    c.execute("INSERT INTO users (email, username, password) VALUES (%s, %s, %s)", (email, username, password))
    conn.commit()

    return jsonify({'message': 'Registration successful.'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

# Check if the username and password match the records in the database
    c.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username, password))
    user = c.fetchone()

    # for email, user_data in registered_users.items():
    #     if user_data['username'] == username and user_data['password'] == password:
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else: 
        return jsonify({'error': 'Invalid username or password'}), 401

# if __name__ == '__main__':
#      app.run(port=3002, debug=True)

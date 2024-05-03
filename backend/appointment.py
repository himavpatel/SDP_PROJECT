import mysql.connector
from flask import Flask,Blueprint, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='sdp'  # Name of your MySQL database in MySQL Workbench
)
c = conn.cursor()

@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    time = data.get('time')
    

    # Insert the new appointment details into the database
    c.execute("INSERT INTO appointments (name, date, time) VALUES (%s, %s, %s)", (name, date, time))
    conn.commit()

    return jsonify({'message': 'Appointment scheduled successfully.'}), 200

if __name__ == '__main__':
     app.run(port=3003, debug=True)

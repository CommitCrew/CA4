from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Connect to MySQL using a context manager
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='commitcrew123',
            database='studentInfo'
        ) as db:
            cursor = db.cursor()

            cursor.execute('SELECT * FROM students')
            data = cursor.fetchall()

            return jsonify(data)
    except Exception as e:
        # Log the error for debugging purposes
        print(e)
        return "An error occurred while processing your request.", 500  # Return a 500 Internal Server Error response

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=80, debug=True)
from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to MySQL
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='studentInfo'
    )
    cursor = db.cursor()

    cursor.execute('SELECT * FROM studentInfo')
    data = cursor.fetchall()

    db.close()

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

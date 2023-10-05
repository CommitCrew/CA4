from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to MySQL
    db = mysql.connector.connect(
        host='mysql_host',
        user='mysql_user',
        password='mysql_password',
        database='mysql_database'
    )
    cursor = db.cursor()

    # Execute SQL queries
    cursor.execute('SELECT * FROM your_table')
    data = cursor.fetchall()

    # Close the database connection
    db.close()

    # Return data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

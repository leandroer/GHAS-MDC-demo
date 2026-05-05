# SQL Injection Vulnerability Example
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search_user():
    """Vulnerable to SQL injection"""
    user_input = request.args.get('username')
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    
    # VULNERABILITY: Direct string concatenation in SQL query
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    
    return str(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

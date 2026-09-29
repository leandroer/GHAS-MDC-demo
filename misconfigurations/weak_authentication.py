# Weak Authentication Implementation
from flask import Flask, request, session
import hashlib

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # VULNERABILITY: Using weak MD5 hash for password comparison
    password_hash = hashlib.md5(password.encode()).hexdigest()
    
    stored_hash = get_user_hash(username)
    
    if password_hash == stored_hash:
        # VULNERABILITY: Session token is predictable
        session['user_id'] = hash(username) % 1000
        session['username'] = username
        return 'Login successful'
    
    return 'Invalid credentials', 401

@app.route('/api/data')
def get_data():
    # VULNERABILITY: No CSRF protection
    user_id = session.get('user_id')
    if not user_id:
        return 'Unauthorized', 401
    
    return {'data': get_sensitive_data(user_id)}

if __name__ == '__main__':
    # Disable debug in production and bind to localhost
    app.run(debug=False, host='127.0.0.1')

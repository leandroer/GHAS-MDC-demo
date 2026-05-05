# Path Traversal Vulnerability
from flask import Flask, request, send_file
import os

app = Flask(__name__)
BASE_DIR = '/var/www/uploads'

@app.route('/download')
def download_file():
    """Path traversal vulnerability"""
    filename = request.args.get('file')
    
    # VULNERABILITY: No validation of filename - allows ../../../etc/passwd
    filepath = os.path.join(BASE_DIR, filename)
    
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return 'File not found', 404

if __name__ == '__main__':
    app.run(debug=True)

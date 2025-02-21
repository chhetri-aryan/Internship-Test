from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    system_username = os.getenv('USER') or os.getenv('USERNAME')

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    top_output = subprocess.getoutput('top -b -n 1 | head -20')

    return f"""
    <h1>System Info</h1>
    <p><b>Name:</b> Aryan Chhetri</p>
    <p><b>Username:</b> {system_username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

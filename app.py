from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# Database path for Docker volume mounting
DB_PATH = os.getenv('DB_PATH', 'focus_sessions.db')

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            vibe TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_session', methods=['POST'])
def save_session():
    data = request.json
    task = data.get('task', '')
    vibe = data.get('vibe', '')
    
    if not task:
        return jsonify({'error': 'Task is required'}), 400
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sessions (task, vibe) VALUES (?, ?)', (task, vibe))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

@app.route('/get_sessions')
def get_sessions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT task, vibe, timestamp FROM sessions ORDER BY timestamp DESC LIMIT 10')
    sessions = cursor.fetchall()
    conn.close()
    
    session_list = []
    for session in sessions:
        session_list.append({
            'task': session[0],
            'vibe': session[1],
            'timestamp': session[2]
        })
    
    return jsonify(session_list)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
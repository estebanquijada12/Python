import sqlite3
import datetime as dt

DB_PATH = "pomodoro_history.db"

def db_init():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pomodoro_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            tarea TEXT NOT NULL,
            duracion INTEGER NOT NULL
        )
    ''')
    conn.commit()
    
def guardar(tarea: str, duracion: int):
    time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pomodoro_sessions (timestamp, tarea, duracion)
            VALUES (?, ?, ?)
        ''', (time, tarea, duracion))
        conn.commit()
    

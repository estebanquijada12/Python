from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI(title="Pomodoro API")
DB_PATH = "pomodoro_history.db"

class sesion(BaseModel):
    tarea: str
    duracion: int
    
def DB_init():
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
@app.on_event("startup")   
def iniciar():
    DB_init()

@app.post("/sesion")
def guardar(sesion: sesion):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pomodoro_sessions (timestamp, tarea, duracion)
            VALUES (?, ?, ?)
        ''', (time, sesion.tarea, sesion.duracion))
        conn.commit()
    return {"status": "success", "message": "Sesión guardada correctamente."}

@app.get("/sesion")
def obtener_sesiones():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pomodoro_sessions ORDER BY timestamp DESC")
    filas = cursor.fetchall()
    columnas = ["id", "timestamp", "tarea", "duracion"]
    
    # zip() empareja cada nombre de columna con su valor correspondiente de la tupla
    return [dict(zip(columnas, fila)) for fila in filas]
import requests

API_URL = "http://localhost:8000/sesion"


import sqlite3
import datetime as dt

DB_PATH = "pomodoro_history.db"

def db_init():
    pass ## la función db_init ya no es necesaria, ya que la inicialización de la base de datos se realiza en la API
    
def guardar(tarea: str, duracion: int):
    payload = {
        "tarea": tarea,
        "duracion": duracion
    }
    try: 
        request = requests.post(API_URL, json=payload)
    except requests.exceptions.ConnectionError as e:
        print(f"Error de conexión al guardar la sesión en la API: {e}")

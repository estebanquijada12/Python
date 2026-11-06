import sqlite3
from datetime import datetime, timedelta
import random

DB_PATH = "pomodoro_history.db"

# Tareas personalizadas para que tu panel de Streamlit se vea real
tareas = [
    "Estudiar",
    "Cuestionarios",
    "Ejercicios",
    "Flash cards"
]

def generar_datos():
    print("🌱 Poblando base de datos con datos realistas...")
    
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        
        # Asegurarnos de que la tabla existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pomodoro_sessions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        tarea TEXT NOT NULL,
                        duracion INTEGER NOT NULL
                    )
        ''')
        
        # Limpiamos la tabla para no duplicar si lo corres varias veces
        cursor.execute("DELETE FROM pomodoro_sessions")
        
        now = datetime.now()
        
        # Generar datos para los últimos 7 días
        for day_offset in range(7, -1, -1):
            current_date = now - timedelta(days=day_offset)
            
            # De 3 a 7 pomodoros por día para que las gráficas tengan volumen
            num_pomodoros = random.randint(3, 7)
            
            # Asumimos que empiezas a trabajar tipo 10:00 AM
            hora_actual = current_date.replace(hour=10, minute=random.randint(0, 30), second=0)
            
            for _ in range(num_pomodoros):
                tarea_actual = random.choice(tareas)
                
                # 1. Registrar Sesión de Trabajo (25 min)
                timestamp_str = hora_actual.strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(
                    "INSERT INTO pomodoro_sessions (timestamp, tarea, duracion) VALUES (?, ?, ?)",
                    (timestamp_str, tarea_actual, 25)
                )
                
                # Avanzar 25 minutos en el tiempo
                hora_actual += timedelta(minutes=25)
                
                # 2. Registrar Sesión de Descanso (5 min)
                timestamp_descanso = hora_actual.strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(
                    "INSERT INTO pomodoro_sessions (timestamp, tarea, duracion) VALUES (?, ?, ?)",
                    (timestamp_descanso, "Descanso", 5)
                )
                
                # Avanzar 5 minutos + un margen aleatorio (te fuiste a preparar un café, etc.)
                hora_actual += timedelta(minutes=5 + random.randint(2, 15))
                
        conn.commit()
        print("✅ ¡Base de datos poblada con éxito! Recarga tu panel de Streamlit.")

if __name__ == "__main__":
    generar_datos()

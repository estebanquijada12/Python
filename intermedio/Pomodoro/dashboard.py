import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000/sesion"

st.set_page_config(page_title="Pomodoro Stats", page_icon="🍅")
st.title("🍅 Panel Pomodoro")

try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        
        if data:
            df = pd.DataFrame(data, columns=['id', 'timestamp', 'tarea', 'duracion'])
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            st.header("Historial de sesiones Pomodoro")
            total_minutos = df['duracion'].sum()
            c1, c2 = st.columns(2)
            c1.metric("Horas Totales", f"{round(total_minutos / 60, 1)} h")
            c2.metric("Pomodoros Completados", len(df))
            
            st.header("Tiempo dedicado por tarea")
            
            if not df.empty:
                resum = df.groupby('tarea')['duracion'].sum().reset_index()
                st.bar_chart(resum, x='tarea', y='duracion', color="#00FFFF")
            
            st.header("Historial detallado")
            st.dataframe(df[['tarea', 'duracion']], use_container_width=True)
        
    else:
        st.info("No hay sesiones registradas aún. ¡Vuelve a la terminal y haz tu primer Pomodoro!")
            
except requests.exceptions.ConnectionError:
    st.error("No se pudo conectar a la API. Asegúrate de que FastAPI está corriendo en el puerto 8000.")
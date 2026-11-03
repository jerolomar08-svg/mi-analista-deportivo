import streamlit as st
import requests

# Configuración de la ventana del chat
st.set_page_config(page_title="Mi Analista Deportivo", page_icon="⚽")
st.title("⚽ Mi Analista Deportivo Personal")

# Tu API Key oficial
API_KEY = "25dde62359034a75ba0c67c36ef47f62"

# Guardar el historial de la conversación
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes en pantalla
for msg in st.session_state.mensajes:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Entrada de texto del usuario
user_input = st.chat_input("Pregúntame sobre un partido o equipo...")

if user_input:
    st.session_state.mensajes.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        url = 'https://api.football-data.org/v4/competitions/CL/matches'
        headers = {'X-Auth-Token': API_KEY}
        res = requests.get(url, headers=headers)
        
        if res.status_code == 200:
            respuesta = f"Consulta recibida para: '{user_input}'. Conexión con datos de la Champions activa. Procesando métricas..."
        else:
            respuesta = "Error al conectar con la base de datos de partidos."
            
        st.write(respuesta)
        st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
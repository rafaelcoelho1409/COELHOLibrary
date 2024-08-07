import streamlit as st
import sys
import threading
import subprocess
from streamlit.components.v1 import iframe

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .css-18e3th9 {
        padding: 0;
    }
    .css-1d391kg {
        padding: 0;
        margin: 0;
    }
    .main .block-container {
        padding: 0;
    }
    iframe {
        width: 100%;
        height: calc(100vh - 32px); /* Set height to full viewport minus title height */
        border: none;
        overflow: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def run_dash():
    #command = """
    #if [[ ! -d coelholibrary_env ]]; then
    #python3 -m venv coelholibrary_env
    #source coelholibrary_env/bin/activate
    #pip install -r requirements.txt"""
    #result = subprocess.run(
    #    command, 
    #    shell = True, 
    #    capture_output = True, 
    #    text = True)
    #print(result)
    subprocess.run([sys.executable, "dash_app.py"])

dash_thread = threading.Thread(target = run_dash)
dash_thread.start()

iframe("http://localhost:8050")
#st.components.v1.iframe("http://localhost:8050", width = 500, height = 500, scrolling = True)
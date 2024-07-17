import streamlit as st
import threading
import subprocess

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
    #subprocess.run(["python3", "dash_app.py"])
    subprocess.run(["pip", "list"])

dash_thread = threading.Thread(target = run_dash)
dash_thread.start()

st.components.v1.iframe("http://localhost:8050", width = None, height = None, scrolling = True)
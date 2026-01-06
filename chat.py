import streamlit as st
from click import prompt, echo

with st.sidebar:
    message = st.container(height=300)
    if prompt := st.chat_input("say something"):
        message.chat_message("user").write(prompt)
        message.chat_message("assistant").write(f"Echo: {prompt}"python -m pip install streamlit==1.24.0)
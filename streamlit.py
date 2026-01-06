"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

if "chat" not in st.session_state:
    st.session_state.chat = []


def process_prompt(prompt):
  st.session_state.chat.append("Job Ready Programmer : "+prompt)
  ## ask gemini
  gemini_response="Gemini : Hello from Gemini!"
  st.session_state.chat.append(gemini_response)
  show_messages()
  return

def show_messages():
  for i in range(len(st.session_state.chat)):
    if(i%2==0):
      with st.chat_message("user"):
        st.write(st.session_state.chat[i])
    else:
      with st.chat_message("assistant"):
        st.write(st.session_state.chat[i])

prompt = st.chat_input("Say something")
if prompt:
    process_prompt(prompt)
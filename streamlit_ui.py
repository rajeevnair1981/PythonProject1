from pydantic_core.core_schema import none_schema

import streamlit as st

st.header('Welcome to blog generator')
st.write('Enter either text or upload image to continue: ')


if "chat" not in st.session_state:
    st.session_state.chat = []
    st.session_state.inputType = ""

class Message:
    def __init__(self, message, Type):
        self.message = message
        self.Type = Type
def input_type_text():
    st.session_state.inputType = 'text'

def process_gemini_response(prompt):
    user_message = Message("User: "+prompt,Type='text')
    st.session_chat.append(user_message)
#gemini integration
    response = "Hi from gemini:"
    gemini_message = Message("Gemini: "+response,Type='text')
    show_messages()
    return

def show_messages():
    for i in range(len(st.session_state.chat)):
        if i%2 == 0:
           with st.chat_message("user"):
                if st.session_state.chat[i].type == "text":
                    st.write(st.session_state.chat[i].message)
        else :
            with st.chat_message("assistant"):
                 st.write(st.session_chat[i].message)
    return

prompt = st.chat_input("enter any topic", on_submit=input_type_text)

if st.session_state.inputType == 'text':
    process_gemini_response(prompt)
    #streaprompt = None


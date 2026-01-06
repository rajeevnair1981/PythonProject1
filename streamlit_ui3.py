import streamlit as st

if "session_chat" not in st.session_state:
    st.session_state.session_chat = []

def process_gemini_response(user_message):
    st.session_state.session_chat.append({"role": "user", "content": user_message})

    # Example response
    response = "Hello! This is a Gemini response."
    st.session_state.session_chat.append({"role": "assistant", "content": response})

# UI
st.title("Chat App")

prompt = st.text_input("Enter your message")

if st.button("Send") and prompt:
    process_gemini_response(prompt)

# Display chat
for msg in st.session_state.session_chat:
    st.write(f"**{msg['role']}**: {msg['content']}")

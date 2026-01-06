import streamlit as st
import base64
import os
from google import genai
from google.genai import types

# Initialize session state
def generate():
    client = genai.Client(
        api_key='AIzaSyCA3EgC2w414op8DwrtTBcy0sSvoWRvLjs',
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=2,
        thinking_config=types.ThinkingConfig(
            thinking_level='HIGH',
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()

if "session_chat" not in st.session_state:
    st.session_state.session_chat = []

def process_gemini_response(user_message):
    st.session_state.session_chat.append({"role": "user", "content": user_message})

    # Example response
    chat_session = types.Part.from_text(text=user_message)
   # response = "Hello! This is a Gemini response."
    st.session_state.session_chat.append({"role": "assistant", "content": chat_session})

# UI
st.title("Chat App")

prompt = st.text_input("Enter your message")

if st.button("Send") and prompt:
    process_gemini_response(prompt)

# Display chat
for msg in st.session_state.session_chat:
    st.write(f"**{msg['role']}**: {msg['content']}")

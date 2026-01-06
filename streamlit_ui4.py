import streamlit as st
import os
from google import genai
from google.genai import types
from google.genai.errors import ClientError

# ---- CONFIG ----
MODEL = "gemini-3-flash-preview"

# Use environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# ---- SESSION STATE ----
if "session_chat" not in st.session_state:
    st.session_state.session_chat = []

# ---- GEMINI CALL ----
def call_gemini(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=4000,
            ),
        )
        return response.text

    except ClientError as e:
        if e.status_code == 429:
            return "⚠️ Quota exceeded. Please wait or reduce usage."
        else:
            return f"❌ Error: {e}"

# ---- UI ----
st.title("💬 Gemini Chat App")

prompt = st.text_input("Enter your message")

if st.button("Send") and prompt:
    st.session_state.session_chat.append(
        {"role": "user", "content": prompt}
    )

    reply = call_gemini(prompt)

    st.session_state.session_chat.append(
        {"role": "assistant", "content": reply}
    )

# ---- DISPLAY CHAT ----
for msg in st.session_state.session_chat:
    st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")

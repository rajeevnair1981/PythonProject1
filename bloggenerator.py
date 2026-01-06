# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
import google.generativeai as genai
from genai import types

def generate():
    client = genai.configure(
        #api_key=os.environ.get("GEMINI_API_KEY"),
        api_key='AIzaSyCA3EgC2w414op8DwrtTBcy0sSvoWRvLjs'
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Kerala"""),
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
            thinking_level="HIGH",
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

import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact about Python."},
    ]
)

print(response.choices[0].message.content)

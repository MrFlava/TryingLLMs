import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you today?"}
]

# Make the API call
response = client.chat.completions.create(model="gpt-3.5-turbo",  # Or "gpt-4" for more advanced capabilities
messages=messages)

# Extract and print the assistant's reply
assistant_message = response.choices[0].message
print(f"{assistant_message['role']}: {assistant_message['content']}")

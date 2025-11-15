import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("GEMINI_API_KEY environment variable not set.")
    exit()

# Choose a model (e.g., 'gemini-1.5-flash')
model = genai.GenerativeModel('gemini-2.5-flash')

# Generate content
prompt = "Explain the concept of quantum entanglement in simple terms."
response = model.generate_content(prompt)

# Print the generated text
print(response.text)
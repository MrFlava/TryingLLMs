import google.generativeai as genai

from settings import API_KEY

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("API_KEY environment variable not set.")
    exit()

model = genai.GenerativeModel('gemini-2.5-flash')
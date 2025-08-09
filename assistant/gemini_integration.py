import google.generativeai as genai
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def generate_question():
    prompt = "Generate a common technical or HR interview question."
    response = model.generate_content(prompt)
    return response.text.strip()

def evaluate_answer(answer):
    prompt = f"Evaluate this interview answer: \"{answer}\". Give constructive feedback."
    response = model.generate_content(prompt)
    return response.text.strip()

# gemini_integration.py



# Load environment variables from .env file



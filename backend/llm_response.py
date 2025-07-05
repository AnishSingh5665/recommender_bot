# backend/llm_response.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set the correct model name
MODEL_NAME = "models/gemini-1.5-flash"

def get_llm_feedback(code):
    prompt = f"""
    Analyze this Python code and provide:
    1. Strengths in logic, structure, or optimization
    2. Weaknesses or areas for improvement
    3. One similar LeetCode-style problem to try next
    4. Concepts to focus on
    5. One helpful video and one article

    Code:
    {code}
    """

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content([{"role": "user", "parts": [{"text": prompt}]}])
        return {"llm_feedback": response.text}
    except Exception as e:
        return {"error": str(e)}

# backend/llm_response.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_llm_feedback(code):
    prompt = f"""
    Analyze this Python code and give feedback:
    
    1. Strengths in terms of logic, structure, readability
    2. Weaknesses or edge cases missed
    3. Suggest next similar LeetCode-style problem
    4. Suggest related concepts to learn
    5. Suggest 2 resources (1 video, 1 article)
    
    Code:
    {code}
    """
    try:
        response = model.generate_content(prompt)
        return {"llm_feedback": response.text}
    except Exception as e:
        return {"error": str(e)}

# backend/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from code_analysis import analyze_code
from embedding_model import generate_embedding
from llm_response import get_llm_feedback
from learning_plan import generate_learning_plan
from storage import save_user_progress

app = FastAPI(title="AI-Powered Coding Mentor")

# CORS for frontend support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_code_endpoint(file: UploadFile = File(...)):
    # Step 0: Read uploaded file
    code = (await file.read()).decode("utf-8")

    # Step 1: Analyze code structure (AST)
    analysis = analyze_code(code)

    # Step 2: Generate embedding (optional for future use)
    embedding = generate_embedding(code)

    # Step 3: Get feedback from LLM
    feedback_response = get_llm_feedback(code)
    feedback_text = feedback_response.get("llm_feedback") if isinstance(feedback_response, dict) else str(feedback_response)

    # Step 4: Generate dynamic learning plan based on feedback
    roadmap = generate_learning_plan(analysis, feedback_text)

    # Step 5: Save user data
    save_user_progress(code, roadmap)

    # Step 6: Return structured response
    return {
        "analysis": analysis,
        "llm_feedback": feedback_text,
        "learning_plan": roadmap
    }

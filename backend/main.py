# backend/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from code_analysis import analyze_code
from embedding_model import generate_embedding
from llm_response import get_llm_feedback
from learning_plan import generate_learning_plan
from storage import save_user_progress

app = FastAPI(title="AI-Powered Coding Mentor")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_code_endpoint(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8")

    # Step 1: Analyze code structure
    analysis = analyze_code(code)

    # Step 2: Generate code embeddings
    embedding = generate_embedding(code)

    # Step 3: Get feedback from LLM
    feedback = get_llm_feedback(code)

    # Step 4: Generate learning plan
    roadmap = generate_learning_plan(analysis, feedback)

    # Step 5: Save data
    save_user_progress(code, roadmap)

    return {
        "analysis": analysis,
        "llm_feedback": feedback,
        "learning_plan": roadmap
    }
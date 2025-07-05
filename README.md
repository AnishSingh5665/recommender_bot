# 🧠 AI Coding Mentor — Personalized Learning Recommender for Coding Students

An AI-powered platform that analyzes coding solutions (e.g., from LeetCode) and provides personalized feedback, learning plans, and study resources to improve coding interview readiness.

---

## 🚀 Features

- 🧠 Code Analysis using AST
- 🤖 Personalized Feedback using LLM (Gemini / HuggingFace)
- 📚 Tailored Learning Plan and Resources
- 🧭 Weekly Goals
- 🌐 Streamlit-based Frontend with Navigation Tabs

---

## 🧰 Tech Stack

| Component      | Tools                            |
|----------------|----------------------------------|
| Frontend       | Streamlit                        |
| Backend        | FastAPI                          |
| Embedding      | CodeBERT (HuggingFace)           |
| LLM Response   | Gemini Pro (Google AI Studio)    |
| Vector Search  | FAISS (Optional – Coming Soon)   |
| Storage        | JSON / SQLite                    |

---

## 🗂️ Project Structure

project-root/
├── backend/
│ ├── main.py
│ ├── code_analysis.py
│ ├── embedding_model.py
│ ├── llm_response.py
│ ├── learning_plan.py
│ ├── storage.py
│ └── requirements.txt
│
├── database/
│ └── users.json
│
├── frontend/
│ └── streamlit_app.py
│
├── .env
└── README.md

yaml
Copy
Edit

---

## 🧪 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-coding-mentor.git
cd ai-coding-mentor
2️⃣ Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv .venv
.\.venv\Scripts\activate      # On Windows
# OR
source .venv/bin/activate     # On macOS/Linux
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r backend/requirements.txt
pip install streamlit python-dotenv
4️⃣ Add Gemini API Key (optional)
Create a .env file in root:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
🔧 Run the Project
▶️ Run Backend
bash
Copy
Edit
cd backend
uvicorn main:app --reload
▶️ Run Frontend
bash
Copy
Edit
cd ../frontend
streamlit run streamlit_app.py
Visit http://localhost:8501 to use the app.

 Replace mocked LLM with real Gemini/Groq responses

 Implement FAISS for similar problem recommendations

 Add user login and history tracking

 Deploy on Streamlit Sharing / Render


🧑‍💻 License
MIT License. Fork, use, contribute freely.

-

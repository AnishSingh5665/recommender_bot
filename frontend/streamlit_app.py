# frontend/streamlit_app.py

import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://127.0.0.1:8000/analyze/"

st.set_page_config(page_title="AI Coding Mentor", page_icon="🤖", layout="wide")

# Sidebar navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📖 About Us", "📬 Contact", "🧠 Code Analyzer"])

# ----- PAGE: HOME -----
if page == "🏠 Home":
    st.title("Welcome to Your AI Coding Mentor 🤖")
    st.write("""
    This platform helps students learn programming smarter with:
    - 📈 Personalized learning plans
    - 🧠 Code feedback and improvement areas
    - 📚 Hand-picked resources
    - 🎯 Weekly goals to sharpen coding skills

    Start your journey by navigating to the "🧠 Code Analyzer" tab!
    """)

# ----- PAGE: ABOUT US -----
elif page == "📖 About Us":
    st.title("About Us 📖")
    st.markdown("""
    **AI Coding Mentor** is built to support students who are preparing for interviews and coding rounds on platforms like LeetCode, HackerRank, and CodeChef.

    Our mission:
    - Detect strengths & weaknesses in your code
    - Recommend the right problems next
    - Guide you like a mentor with LLM-powered advice

    Built using:
    - Python (FastAPI, Streamlit)
    - Hugging Face / Gemini
    - FAISS for code similarity
    """)

# ----- PAGE: CONTACT -----
elif page == "📬 Contact":
    st.title("Contact Us 📬")
    st.write("""
    Feel free to reach out for feedback, suggestions, or collaboration opportunities!
    
    📧 Email: support@aicodingmentor.dev  
    💬 LinkedIn: [LinkedIn Profile](https://linkedin.com/in/your-profile)  
    🛠 GitHub: [Project Repository](https://github.com/your-repo)
    """)

# ----- PAGE: CODE ANALYZER -----
elif page == "🧠 Code Analyzer":
    st.title("🧠 Analyze Your Code")
    st.write("Upload your Python solution file (e.g., from LeetCode) and get personalized feedback!")

    uploaded_file = st.file_uploader("Upload your `.py` code file", type=["py"])

    if uploaded_file is not None:
        st.success("File uploaded successfully! Analyzing...")

        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            result = response.json()
            
            st.subheader("📊 Code Analysis")
            st.write(result.get("analysis", {}))

            st.subheader("🧠 LLM Feedback")
            llm = result.get("llm_feedback", {})
            if isinstance(llm, dict):
                st.json(llm)
            else:
                st.markdown(llm.replace("\n", "  \n"))

            st.subheader("🎯 Learning Plan")
            plan = result.get("learning_plan", {})
            st.write(f"**Next Problem:** {plan.get('next_problem')}")
            st.write(f"**Concepts to Learn:** {', '.join(plan.get('concepts_to_learn', []))}")
            st.write(f"**Weekly Goal:** {plan.get('weekly_goal')}")

            st.write("**Resources:**")
            for res in plan.get("resources", []):
                st.markdown(f"- [{res['title']}]({res['link']}) ({res['type']})")
        else:
            st.error("❌ Something went wrong with the analysis API.")

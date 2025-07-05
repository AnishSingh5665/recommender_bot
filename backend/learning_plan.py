# backend/learning_plan.py

import re

def extract_learning_plan(llm_text: str):
    next_problem = ""
    concepts = []
    resources = []
    weekly_goal = ""

    # Extract next problem
    match = re.search(r"(LeetCode\s*#\d+\s*[-–—]?\s*[\w\s]+)", llm_text, re.IGNORECASE)
    if match:
        next_problem = match.group(1).strip()

    # Extract concepts
    concepts_match = re.findall(r"(?:\d\.\s*)?(Concepts|Focus|Topics)[^:]*:\s*(.+)", llm_text, re.IGNORECASE)
    for _, line in concepts_match:
        parts = re.split(r",|\n|-", line)
        concepts.extend([p.strip() for p in parts if p.strip()])

    # Extract links as resources
    links = re.findall(r"(https?://[^\s]+)", llm_text)
    for link in links:
        if "youtube" in link or "youtu.be" in link:
            resources.append({"type": "video", "title": "Video Resource", "link": link})
        else:
            resources.append({"type": "article", "title": "Article Resource", "link": link})

    # Extract weekly goal
    goal_match = re.search(r"(weekly goal.*?:.*)", llm_text, re.IGNORECASE)
    if goal_match:
        weekly_goal = goal_match.group(1).strip()

    return {
        "next_problem": next_problem,
        "concepts_to_learn": concepts[:3],
        "resources": resources[:2],
        "weekly_goal": weekly_goal
    }

def generate_learning_plan(analysis, feedback):
    """
    Parses Gemini output and returns structured learning plan.
    """
    if isinstance(feedback, dict) and "llm_feedback" in feedback:
        feedback_text = feedback["llm_feedback"]
    else:
        feedback_text = feedback if isinstance(feedback, str) else str(feedback)

    return extract_learning_plan(feedback_text)

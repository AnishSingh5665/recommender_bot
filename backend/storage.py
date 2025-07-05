# backend/storage.py

import json
import os

DB_FILE = "database/users.json"

def save_user_progress(code, roadmap):
    if not os.path.exists("database"):
        os.mkdir("database")

    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

    with open(DB_FILE, "r") as f:
        data = json.load(f)

    data.append({
        "code": code,
        "roadmap": roadmap
    })

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

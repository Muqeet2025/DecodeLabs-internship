import json
import os

FILE_PATH = "data/tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    os.makedirs("data", exist_ok=True)  # auto create folder
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)
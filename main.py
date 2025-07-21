# main.py
# Lobos One — первая версия
# Создано Стражем Галактики (Moustopoulos Aristide’s)

import json
from datetime import datetime

DATA_FILE = "thoughts.json"

def save_thought(thought, author="Anonymous"):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            thoughts = json.load(f)
    except FileNotFoundError:
        thoughts = []

    new_thought = {
        "author": author,
        "thought": thought,
        "timestamp": datetime.utcnow().isoformat()
    }

    thoughts.append(new_thought)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(thoughts, f, indent=4, ensure_ascii=False)

    print("✅ Thought saved.")

# Пример использования
if __name__ == "__main__":
    user_input = input("Enter your thought: ")
    save_thought(user_input, author="Страж Галактики")

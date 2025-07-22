# lobos_one_alpha/main.py
# Первый прототип Lobos One — обучающийся алгоритм смыслов

import json
import uuid
from datetime import datetime

# Хранилище мыслей (в будущем будет база данных)
data_store = "thoughts.json"


def load_data():
    try:
        with open(data_store, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(thoughts):
    with open(data_store, "w", encoding="utf-8") as f:
        json.dump(thoughts, f, ensure_ascii=False, indent=2)


def add_thought(text, tags=None, language="auto"):
    thought = {
        "id": str(uuid.uuid4()),
        "text": text.strip(),
        "tags": tags or [],
        "language": language,
        "timestamp": datetime.utcnow().isoformat()
    }
    thoughts = load_data()
    thoughts.append(thought)
    save_data(thoughts)
    return thought


def get_similar_thoughts(query):
    # Заглушка: просто возвращаем 3 случайные мысли
    import random
    thoughts = load_data()
    return random.sample(thoughts, min(len(thoughts), 3))


# Пример использования
if __name__ == "__main__":
    print("Добро пожаловать в Lobos One Alpha")
    while True:
        user_input = input("\nВведите мысль (или 'exit'): ")
        if user_input.lower() == "exit":
            break
        thought = add_thought(user_input)
        print("Сохранено:", thought)

        print("Похожие мысли:")
        for t in get_similar_thoughts(user_input):
            print("-", t["text"])

    print("До связи. Вы были частью Lobos One.")

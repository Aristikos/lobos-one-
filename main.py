import json
from datetime import datetime

CATEGORIES = [
    "идея",
    "мечта",
    "страх",
    "цель",
    "воспоминание",
    "наблюдение",
    "вопрос"
]

def save_thought(thought, category):
    data = {
        "text": thought,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category
    }

    try:
        with open("thoughts.json", "r", encoding="utf-8") as f:
            thoughts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        thoughts = []

    thoughts.append(data)

    with open("thoughts.json", "w", encoding="utf-8") as f:
        json.dump(thoughts, f, ensure_ascii=False, indent=2)

def choose_category():
    print("\nВыбери категорию:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
    while True:
        choice = input("Введи номер категории: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        else:
            print("Неверный ввод. Попробуй снова.")

def show_all_thoughts():
    try:
        with open("thoughts.json", "r", encoding="utf-8") as f:
            thoughts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\n📭 Нет сохранённых мыслей.")
        return

    print("\n📒 Все мысли:\n")
    for t in thoughts:
        print(f"[{t['timestamp']}] ({t['category']}) {t['text']}")

def show_by_category():
    cat = choose_category()
    try:
        with open("thoughts.json", "r", encoding="utf-8") as f:
            thoughts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\n📭 Нет сохранённых мыслей.")
        return

    filtered = [t for t in thoughts if t["category"] == cat]

    print(f"\n📘 Мысли категории: {cat}\n")
    if not filtered:
        print("Ничего не найдено.")
    else:
        for t in filtered:
            print(f"[{t['timestamp']}] {t['text']}")

def main_menu():
    while True:
        print("\n🔷 Главное меню:")
        print("1. Добавить новую мысль")
        print("2. Показать все мысли")
        print("3. Показать по категории")
        print("4. Выйти")

        choice = input("Выбери действие: ")

        if choice == "1":
            thought = input("Введи свою мысль: ")
            category = choose_category()
            save_thought(thought, category)
            print("✅ Мысль сохранена.")
        elif choice == "2":
            show_all_thoughts()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            print("👋 До встречи!")
            break
        else:
            print("Неверный ввод. Попробуй снова.")

if __name__ == "__main__":
    main_menu()
1
import sys
from app.core.processor import process_numbers, safe_divide
from app.utils.exceptions import AppError, ValidationError

def run_demonstration():
    print("--- Сценарій 1: Успішна обробка ---")
    data = ["4", "16", "25"]
    print(f"Вхід: {data} -> Результат: {process_numbers(data)}")

    print("\n--- Сценарій 2: Помилка та ланцюжок виключень ---")
    try:
        process_numbers(["4", "abc"])
    except ValidationError as e:
        print(f"Перехоплено доменне виключення: {e}")
        print(f"Першопричина (cause): {e.__cause__}")

    print("\n--- Сценарій 3: Конструкція try/else/finally ---")
    safe_divide(10, 2)
    safe_divide(10, 0)

    print("\n--- Сценарій 4: Контекстний менеджер ---")
    # Демонстрація with як заміни try/finally
    try:
        with open("temp.txt", "w", encoding="utf-8") as f:
            f.write("Тест")
            print("Файл відкрито та записано.")
            # Файл закриється автоматично навіть якщо тут виникне помилка
    except IOError as e:
        print(f"Помилка файлу: {e}")

    print("\n--- Сценарій 5: Інтроспекція (Завдання 4) ---")
    print(f"Документація функції process_numbers:\n{process_numbers.__doc__}")
    print(f"Анотації типів: {process_numbers.__annotations__}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        help(process_numbers)
    else:
        run_demonstration()

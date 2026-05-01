"""Модуль для обробки числових даних із застосуванням виключень."""
from typing import List, Optional
from app.utils.exceptions import ProcessingError, ValidationError

def process_numbers(data: List[str]) -> List[float]:
    """
    Перетворює список рядків у числа та виконує обчислення.

    Args:
        data: Список рядкових значень для обробки.

    Returns:
        Список оброблених чисел.

    Raises:
        ValidationError: Якщо дані мають невірний формат.
        ProcessingError: Якщо виникла критична помилка обробки.
    """
    results = []
    for item in data:
        try:
            val = float(item)
            if val < 0:
                raise ValueError("Число не може бути від'ємним")
            results.append(val ** 0.5)
        except (ValueError, TypeError) as e:
            raise ValidationError(f"Некоректний елемент '{item}'", field="data_list") from e
            
    return results

def safe_divide(a: float, b: float) -> Optional[float]:
    """Виконує безпечне ділення з повною конструкцією try/except/else/finally."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль!")
    else:
        print("Ділення виконано успішно.")
    finally:
        print("Завершення операції ділення.")
    return result

# TODO решите задачу
import json


def task() -> float:
    """
    Функция для чтения JSON файла и поиска суммы произведений двух значений в каждом словаре.
    """
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0  # Инициализируем сумму

    for item in data:  # Проходим по каждому словарю в списке
        product = item.get("score") * item.get("weight")  # Произведение "score" * "weight" в каждом словаре
        total_sum += product  # Cумма этих произведений

    return round(total_sum, 3)  # Округляем и возвращаем сумму с тремя знаками после запятой


print(task())

import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """
    Функция для конвертации файлов из формата CSV в формат JSON.
    """
    with open(INPUT_FILENAME, "r") as cvs_file:  # Считываем содержимое CSV файла
        cvs_data = [row for row in csv.DictReader(cvs_file)]

    with open(OUTPUT_FILENAME, "w") as json_file: # Записываем данные в JSON файл с отступами равными 4
        json.dump(cvs_data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

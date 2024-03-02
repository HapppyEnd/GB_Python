"""Создайте функцию generate_csv_file(file_name, rows), которая будет
генерировать по три случайны числа в каждой строке, от 100-1000 строк,
и записывать их в CSV-файл. Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно
сгенерировать.
Создайте функцию find_roots(a, b, c), которая будет находить корни
квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.
Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
Создайте декоратор save_to_json(func), который будет оборачивать функцию
find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции,
исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью
функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись
JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в
файле results.json будет сохранена информация о параметрах и результатах
вычислений для каждой строки данных из CSV-файла.

"""
import csv
import json
from random import randint


def save_to_json(func):
    """Читает данные из CSV-файла, переданного в аргументе функции,
    исходя из аргумента args[0]. Для каждой строки данных вычисляет
    корни квадратного уравнения с помощью функции find_roots.
    Сохраняет результаты в формате JSON в файл results.json."""
    data = []

    def wrapper(*args, **kwargs):

        with open(args[0], 'r', encoding='utf-8') as file:
            res = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for a, b, c in res:
                a, b, c = int(a), int(b), int(c)
                data.append(
                    {"parameters": [a, b, c], "result": func(a=a, b=b, c=c)})
        with open('results.json', 'w', encoding='utf-8') as res_json:
            json.dump(data, res_json)

    return wrapper


def generate_csv_file(file_name: str, rows: int):
    """Создайте функцию generate_csv_file(file_name, rows), которая будет
    генерировать по три случайны числа в каждой строке, от 100-1000 строк,
    и записывать их в CSV-файл. Функция принимает два аргумента:
    file_name (строка) - имя файла, в который будут записаны данные.
    rows(целое число) - количество строк (записей) данных, которые нужно
    сгенерировать."""
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows([[randint(1, 100) for _ in range(3)]
                         for _ in range(rows)])


@save_to_json
def find_roots(a: int = 1, b: int = 1, c: int = 1) -> None | int:
    """Находит корни квадратного уравнения вида ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2
    if discriminant == 0:
        x1 = -b / (2*a)
        return x1
    return None

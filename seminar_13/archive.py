"""Допишите в вашу задачу Archive обработку исключений.
Добавьте исключение в ваш код InvalidTextError, которые будет вызываться,
когда текст не является строкой или является пустой строкой.
Текст ошибки:
Invalid text: {введенный текст}. Text should be a non-empty string.'
И InvalidNumberError, которое будет вызываться, если число не является
положительным целым числом или числом с плавающей запятой.
Текст ошибки: 'Invalid number:
{введенное число}. Number should be a positive integer or float.'"""
from typing import Any, Union


class InvalidTextError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class InvalidNumberError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'text':
            if not isinstance(__value, str) or __value == '':
                raise InvalidTextError(f'Invalid text: {__value}.'
                                       ' Text should be a non-empty string.')
        if __name == 'number':
            if not isinstance(__value, Union[int, float]) or __value < 0:
                raise InvalidNumberError(
                    f'Invalid number: {__value}. Number should be a '
                    'positive integer or float.')
        super().__setattr__(__name, __value)

    def __str__(self):
        return (f'Text is {self.text} and number is {self.number}.'
                f' Also {self.archive_text} and {self.archive_number}')

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

# Введите ваше решение ниже


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'text':
            if not isinstance(__value, str) or __value == '':
                raise InvalidTextError(f'Invalid text: {__value}.'
                                       ' Text should be a non-empty string.')
        if __name == 'number':
            if not isinstance(__value, (int, float)) or __value < 0:
                raise InvalidNumberError(
                    f'Invalid number: {__value}. Number should be a '
                    'positive integer or float.')
        return super().__setattr__(__name, __value)

    def __str__(self):
        return (f'Text is {self.text} and number is {self.number}.'
                f' Also {self.archive_text} and {self.archive_number}')

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

# Введите ваше решение ниже


invalid_archive_instance = Archive("Sample text", -5)
print(invalid_archive_instance)
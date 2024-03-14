"""В организации есть два типа людей: сотрудники и обычные люди.
Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка,
не пустая) Возраст (целое положительное число) Сотрудники имеют также
уникальный идентификационный номер (ID), который должен быть шестизначным
положительным целым числом.
Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления
данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять
валидность входных данных и генерировать исключения InvalidNameError и
InvalidAgeError, если данные неверные.
Создать класс Employee, который будет наследовать класс Person и добавлять
уникальный идентификационный номер (ID). Класс Employee также должен проверять
валидность ID и генерировать исключение InvalidIdError, если ID неверный.
Добавить метод birthday в класс Person, который будет увеличивать возраст
человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать
уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и
проверить, что исключения работают корректно при передаче неверных данных."""


from typing import Any


class InvalidNameError(Exception):

    def __init__(self, *args) -> None:
        self.args = args

    def __str__(self) -> str:
        return (
            f'Invalid name: {self.args[0]}. Name should be a non-empty string.'
        )


class InvalidAgeError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'Invalid age: {self.value}. Age should be a positive integer.')


class InvalidIdError(Exception):

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return (f'Invalid id: {self.value}. Id should be a 6-digit positive '
                'integer between 100000 and 999999.')


class Person:
    """Class Person."""

    def __init__(self, first_name: str, last_name: str,
                 patronymic: str, age: int) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic

        if age > 0:
            self._age = age
        else:
            raise InvalidAgeError(age)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['first_name', 'last_name', 'patronymic']:
            if not isinstance(__value, str) or __value == '':
                raise InvalidNameError(__value)
        return super().__setattr__(__name, __value)

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def get_age(self):
        return self._age


class Employee(Person):
    """Class Employee."""
    MAX_LEVEL = 7

    def __init__(self, first_name: str, last_name: str, patronymic: str,
                 age: int, id: int) -> None:
        super().__init__(first_name, last_name, patronymic, age)
        self.id = id

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'id':
            if not isinstance(__value, int) or not (
                    100_000 <= __value < 1_000_000):
                raise InvalidIdError(__value)

        return super().__setattr__(__name, __value)

    def get_level(self):
        sum_num = sum(int(num) for num in str(self.id))
        return sum_num % self.MAX_LEVEL


p = Person('1', '4567', '3', 2)
print(p.first_name)
e = Employee('1', '2', '3', -2, 1256)

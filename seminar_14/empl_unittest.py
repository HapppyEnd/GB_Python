import unittest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


class TestEmployee(unittest.TestCase):
    def test_employee_full_name(self):

        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        self.assertEqual(emp.full_name(), "Ivanov Ivan Ivanovich")

    def test_employee_birthday(self):
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        emp.birthday()
        self.assertEqual(emp.get_age(), 31)

    def test_employee_raise_salary(self):
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        emp.raise_salary(10)
        self.assertEqual(round(emp.salary, 1), 55000.0)

    def test_employee_str(self):
        emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        self.assertEqual(str(emp), 'Ivanov Ivan Ivanovich (Manager)')

    def test_employee_last_name_title(self):
        emp = Employee('ivanov', 'ivan', 'ivanovich', 30, 'manager', 50000)
        self.assertEqual(emp.last_name, 'Ivanov')


if __name__ == '__main__':
    unittest.main()

"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв. Если ФИО не соответствует условию, выведите:
ФИО должно состоять только из букв и начинаться с заглавной буквы
○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
Предмет {Название предмета} не найден
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов
(от 0 до 100). В противном случае выведите:
Оценка должна быть целым числом от 2 до 5
Результат теста должен быть целым числом от 0 до 100
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
и по оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл
записана следующая информация.
Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи
по предметам. Класс должен иметь следующие методы:
Атрибуты класса:
name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы
в качестве ключей и информацию об оценках и результатах тестов для каждого
предмета в виде словаря.
"""
import csv


class Student:
    """Student."""

    def __init__(self, name: str, subjects_file: str) -> None:
        """Конструктор класса. Принимает имя студента и файл с предметами
        и их результатами. Инициализирует атрибуты name и subjects и
        вызывает метод load_subjects для загрузки предметов из файла."""
        self.name = name
        self.subjects_file = subjects_file
        self.subjects = {k: {} for k in self.load_subjects(subjects_file)}

    def __setattr__(self, name: str, value: str):
        """Дескриптор, который проверяет установку атрибута name.
        Убеждается, что name начинается с заглавной буквы и состоит
        только из букв."""
        if name == 'name':
            for element in value.split(' '):
                if not element.isalpha() or not element.istitle():
                    raise ValueError(
                        'ФИО должно состоять только из букв и начинаться '
                        'с заглавной буквы')
        super().__setattr__(name, value)

    def __getattr__(self, name):
        """Позволяет получать значения атрибутов предметов
        (оценок и результатов тестов) по их именам."""
        super().__getattribute__(name)

    def __str__(self):
        """Возвращает строковое представление студента, включая имя и
        список предметов. Студент: Иван Иванов Предметы: Математика, История"""
        res = []
        for subject, value in self.subjects.items():
            if value != {}:
                res.append(subject)
        result = ', '.join(res)
        return f'Студент: {self.name}\nПредметы: {result}'

    def load_subjects(self, subjects_file):
        """Загружает предметы из файла CSV. Использует модуль csv для
        чтения данных из файла и добавляет предметы в атрибут subjects."""
        subjects = []
        with open(subjects_file, 'r', encoding='utf-8') as file:
            res = csv.reader(file)
            for i in res:
                for j in i:
                    subjects.append(j)
        return subjects

    def add_grade(self, subject, grade):
        """Добавляет оценку по заданному предмету.
        Убеждается, что оценка является целым числом от 2 до 5."""
        if not isinstance(grade, int) or not 2 <= grade <= 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        if subject in self.load_subjects(self.subjects_file):
            self.subjects.get(subject).setdefault(
                'grades', []).append(grade)

    def add_test_score(self, subject, test_score):
        """Добавляет результат теста по заданному предмету.
        Убеждается, что результат теста является целым числом от 0 до 100."""
        if not isinstance(test_score, int) or not 0 <= test_score <= 100:
            raise ValueError(
                'Результат теста должен быть целым числом от 0 до 100')
        if subject in self.load_subjects(self.subjects_file):
            self.subjects.get(subject).setdefault(
                'test_scores', []).append(test_score)

    def get_average_test_score(self, subject):
        """Возвращает средний балл по тестам для заданного предмета."""
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        res = self.subjects[subject]['test_scores']
        if not (length := len(res)):
            return 0
        return sum(res)/length

    def get_average_grade(self):
        """Возвращает средний балл по всем предметам."""
        count = 0
        aver = 0
        for i in self.subjects.values():
            if i != {}:
                for j in i.get('grades'):
                    count += 1
                    aver += j
        if not count:
            return 0
        return aver/count


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

"""Разработайте программу для работы с прямоугольниками. Необходимо создать
класс Rectangle, который будет представлять прямоугольник с заданными
шириной и высотой.
Атрибуты класса:
width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
Методы класса:
__init__(self, width, height=None): Конструктор класса. Принимает ширину
и высоту прямоугольника. Если высота не указана (по умолчанию None), то
считается, что прямоугольник является квадратом, и высота устанавливается
равной ширине.
perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает
целое число - значение периметра.
area(self): Метод для вычисления площади прямоугольника. Возвращает целое
число - значение площади.
Метод __add__ объединяет два прямоугольника по периметру и создает
новый прямоугольник.
Метод __sub__ вычитает один прямоугольник из другого, представляя разницу
периметров исходных прямоугольников, и создает новый прямоугольник.
Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их
площади.
Методы __str__ и __repr__ предоставляют строковое представление объекта
класса Rectangle."""


class Rectangle:
    """Class rectangle."""

    def __init__(self, width: int, height: int = None) -> None:
        self.width = width
        if height:
            self.height = height
        else:
            self.height = width

    def perimeter(self) -> int:
        """Периметр."""
        return (self.width + self.height) * 2

    def area(self) -> int:
        """Площадь."""
        return self.width * self.height

    def __add__(self, other):
        perimeter = self.perimeter() + other.perimeter()
        width = self.width + other.width
        height = perimeter//2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        perimeter = self.perimeter() - other.perimeter()
        if self.width > self.height:
            self.width, self.height = self.height, self.width
        if other.width > other.height:
            other.width, other.height = other.height, other.width
        width = self.width - other.width
        height = perimeter//2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")

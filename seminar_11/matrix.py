"""Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые
операции с матрицами.
Атрибуты класса:
rows (int): Количество строк в матрице.
cols (int): Количество столбцов в матрице.
data (list): Двумерный список, содержащий элементы матрицы.
Методы класса:
__init__(self, rows, cols): Конструктор класса, который инициализирует
атрибуты rows и cols, а также создает двумерный список data размером rows
x cols и заполняет его нулями.
__str__(self): Метод, возвращающий строковое представление матрицы.
Возвращаемая строка представляет матрицу, где элементы разделены
пробелами, а строки разделены символами новой строки. Например:
1 2 3
4 5 6
__repr__(self): Метод, возвращающий строковое представление объекта
которое может быть использовано для создания нового объекта того же класса
с такими же размерами и данными.
__eq__(self, other): Метод, определяющий операцию "равно" для двух матриц.
Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество
строк и столбцов, а также все элементы равны. Иначе возвращает False.
__add__(self, other): Метод, определяющий операцию сложения двух матриц.
Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и
столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент
равен сумме соответствующих элементов входных матриц.
__mul__(self, other): Метод, определяющий операцию умножения двух матриц.
Проверяет, что количество столбцов в первой матрице равно количеству
строк во второй матрице. Если условие выполняется, создает новую матрицу,
где элемент на позиции [i][j] равен сумме произведений элементов
соответствующей строки из первой матрицы и столбца из второй матрицы."""


class Matrix:
    """Matrix."""

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(self.rows)] for _ in range(self.cols)]

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, elem))for elem in self.data])

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.rows}, {self.cols})'

    def __eq__(self, other: object) -> bool:
        return (self.rows == other.rows and
                self.cols == other.cols and self.data == other.data)

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            res = Matrix(self.rows, self.cols)
            res.data = [[self.data[i][j] + other.data[i][j]
                         for j in range(len(self.data[0]))]
                        for i in range(len(self.data))]
            return res
        raise ValueError('Матрицы должны быть одинакового размера.')

    def __mul__(self, other):
        if self.cols == other.rows:
            res = Matrix(self.rows, other.cols)
            res.data = [[sum(i * j for i, j in zip(row_a, col_b)) for
                         col_b in zip(*other.data)] for row_a in self.data]
            return res
        raise ValueError(
            'Kоличество столбцов в первой матрице должно быть равно количеству'
            'строк во второй матрице.')

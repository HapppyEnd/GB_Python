"""Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
"""

NUMBER = 10
matrix = [[' ' for _ in range(NUMBER*2-1)] for _ in range(NUMBER)]
for i, elem in enumerate(matrix):
    middle = len(matrix[i])//2
    matrix[i][middle] = '*'
    if i == 0:
        start, end = middle, middle
        continue
    start -= 1
    end += 1
    for k in range(start, end + 1):
        matrix[i][k] = '*'


def print_matrix(mat):
    """Print matrix."""
    for row in mat:
        for col in row:
            print(col, end=' ')
        print()


print_matrix(matrix)

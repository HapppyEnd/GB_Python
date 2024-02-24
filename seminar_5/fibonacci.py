"""Создайте функцию генератор чисел Фибоначчи fibonacci."""


def fibonacci():
    """Генератор чисел Фибоначчи."""
    a = 0
    b = 1
    while True:
        if not a:
            yield a
        a, b = b, a + b
        yield a


f = fibonacci()
for i in range(10):
    print(next(f))

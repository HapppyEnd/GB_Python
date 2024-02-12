"""Программа загадывает число от 0 до 1000. Необходимо угадать число
за 10 попыток. Программа должна подсказывать «больше» или «меньше» после
каждой попытки. Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT) """
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 100
limit: int = 2
num: int = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

while limit >= 0:
    if limit == 0:
        print(f'попытки закончились!Вы не угадали. Загаданное число {num}')
        break
    try:
        number: int = int(input('Угадайте число:'))
        if number > num:
            print('Загаданное число меньше вашего')
            print(f'Осталось {limit} попыток.')
        elif number < num:
            print('Загаданное число больше вашего')
            print(f'Осталось {limit} попыток.')
        else:
            print('Угадали!')
            break
        limit -= 1
    except ValueError:
        print('Некорректный ввод')

"""Задание №7
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print"""

number: int = int(input('Input number from 1 to 999: '))

MIN_NUMBER = 1
MAX_NUMBER = 999
DOUBLE_DIGIT = 10
THREE_DIGIT = 100
if number < MIN_NUMBER or number > MAX_NUMBER:
    print('Incorrect input.')
elif MIN_NUMBER <= number < DOUBLE_DIGIT:
    print(f'Your number: {number} - square: {number**2}')
elif DOUBLE_DIGIT <= number < THREE_DIGIT:
    print(
        f'Your number: {number} - multiply: {(number // 10) * (number % 10)}')
else:
    res = list(str(number))
    if res[-1] == '0':
        res.remove(res[-1])
        if res[-1] == '0':
            res.remove(res[-1])

    print(f'Your number: {number} - reflect: {"".join(map(str, res[::-1]))}')

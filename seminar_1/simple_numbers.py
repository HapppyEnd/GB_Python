"""Напишите код, который запрашивает число и сообщает является ли оно
простым или составным. Используйте правило для проверки: «Число является
простым, если делится нацело только на единицу и на себя». Сделайте
ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

MIN_NUMBER = 2
MAX_NUMBER = 100000


while True:
    number: str = input('Введите число или q для выхода: ')
    if number == 'q':
        print('До свидания!')
        break
    try:
        number = int(number)
        if number < MIN_NUMBER or number > MAX_NUMBER:
            print(f'Введите число из диапазона {MIN_NUMBER} - {MAX_NUMBER}.')
        else:
            for num in range(2, int(number/2) + 1):
                if number % num == 0:
                    print('Число является составным.')
                    break
            else:
                print('Число является простым.')
    except ValueError:
        print('Некорректный ввод! Введите число или q для выхода.')

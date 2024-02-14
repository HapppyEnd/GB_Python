""" Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
"""
CONST_HEX = 16
num: int = 123456


def dec_to_hex(number: int):
    result = []
    alp = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while number > 0:
        result.append(str(alp[number % CONST_HEX]))
        number //= CONST_HEX
    return "".join(result[::-1])


num_hex: str = dec_to_hex(num)

print(f"""
Шестнадцатеричное представление числа: {num_hex}
Проверка результата: {hex(num)}""")

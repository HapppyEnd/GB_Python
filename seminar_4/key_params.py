"""Напишите функцию key_params, принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ - значение переданного
аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

Пример использования.
На входе:

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
На выходе:

{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}"""


def key_params(**kwargs):
    """Return transpose dict."""
    result_dict = {}
    for key, value in kwargs.items():
        if value.__hash__:
            result_dict[value] = key
        else:
            result_dict[str(value)] = key
    return result_dict


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)

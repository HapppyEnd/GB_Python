"""Дан список повторяющихся элементов lst. Вернуть список с
дублирующимися элементами. В результирующем списке не должно быть
дубликатов."""
lst: list = [1, 1, 2, 2, 3, 3, 4, 5, 6, 5, 5, 5]
res_list: list = []
for item in set(lst):
    if lst.count(item) > 1:
        res_list.append(item)
print(res_list)

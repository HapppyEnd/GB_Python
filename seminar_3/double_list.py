"""Дан список повторяющихся элементов lst. Вернуть список с
дублирующимися элементами. В результирующем списке не должно быть
дубликатов."""
import time

lst: list = [1, 1, 2, 2, 3, 3, 4, 5, 6, 5, 5, 5, 'a', 'a']
start_time = time.time()
result_list: list = [i for i in set(lst) if lst.count(i) > 1]
end_time = time.time() - start_time

print(result_list)
print(end_time)
my_list = [1, 1, 1, 1, 2, 3, 4, 1, 3, 2, 4, 5, 7, 8]
print(list(set(my_list)))
11111111                                                                                
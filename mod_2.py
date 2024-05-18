"""
# Задание 2
# в наличии список множеств. внутри множества целые числа
# посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все числа из множеств в один кортеж
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
# *написать решения в одну строку

"""
from functools import reduce


m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
res = reduce(lambda x, y: x.union(y), m)

sum_num = sum(list(map((lambda x: sum(list(x))), m)))
len_set = sum(list(map((lambda x: len(x)), m)))
new_tuple = tuple(reduce(lambda x, y: x + y, list(map((lambda x: list(x)), m))))
print(f'Объединение множеств {res}')
print(f'Сумма чисел множеств {sum_num} количество чисел {len_set} средние значение {sum_num/len_set}')
print(f'Кортеж из множеств {new_tuple}')

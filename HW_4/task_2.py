"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""
from random import randint

# n = int(input("Введите число: "))
my_list = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
print(my_list)
result_list = []

for number in my_list:
    if not my_list.count(number) > 1:
        result_list.append(number)

print(result_list)

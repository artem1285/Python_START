"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
from random import randrange  # randrange возвращает случайное целое число из указанного диапазона (start, stop, step)

size_list = int(input('Введите размер списка: '))
rand_list = [randrange(9) for i in range(size_list)]
result_list1, result_list2, result_list3 = [], [], []
print(rand_list)
for i in range(size_list):
    if rand_list.count(rand_list[i]) == 1:
        result_list1.append(rand_list[i])
    if rand_list.count(rand_list[i]) > 1:
        result_list2.append(rand_list[i])
        result_list2 = [i for n, i in enumerate(
            result_list2) if i not in result_list2[:n]]
result_list3 = [i for n, i in enumerate(rand_list) if i not in rand_list[:n]]
print(result_list1)
print(result_list2)
print(result_list3)

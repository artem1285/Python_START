"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""

from random import randint
number = int(input('Введите число '))
lst = [randint(0, 10) for _ in range(number)]
print(lst)

summa = 0
for i in range(1, number, 2): 
    summa += lst[i]
print(summa)

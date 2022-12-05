"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
from random import uniform  # uniform() возвращает случайный вещественное число
number = int(input('Введите число '))
# round округляtn число с плавающей точкой до той цифры, которую задает пользователь
first_lst = [round(uniform(0, 10), 2) for _ in range(number)]
print(first_lst)
second_lst = [round(first_lst[i] - int(first_lst[i]), 2)
              for i in range(number)]
print(max(second_lst) - min(second_lst))

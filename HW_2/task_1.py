"""
Напишите программу, которая принимает на вход вещественное число и
показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""

num = float(input("Введите число: "))
sum = 0  # переменная, в которую будет записываться сумма
for i in str(num):  # для i в числе
    if i != '.':  # если i не равен (.)
        sum += int(i)  # прибавляем к сумме
print(sum)

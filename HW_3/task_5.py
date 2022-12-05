"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
num = int(input('Введите число: '))


def fib(num):
    fib_num = []
    a, b = 1, 1
    for i in range(num):
        fib_num.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(num+1):
        fib_num.insert(0, a)
        a, b = b, a - b
    return fib_num


fib_num = fib(num)
print(fib(num))

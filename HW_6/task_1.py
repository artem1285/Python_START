"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""
# message = '1 + 2 + 5 + 8' # строка - выражение
# a, symbol, b = message.split() # распакуем списокв в переменные .Symbol — самый важный класс в библиотеке SymPy.
# # символьные вычисления выполняются с помощью символов
# # Symbol проваеряем с плюсом
# if symbol == '+': # если это +, то можем вывести сразу в принт
#     print(float(a) + float(b))


def find(exp, sech_operand):  # Ф которая ищет конкретно знаки * и /
    ind_start = 0
    ind_finish = 0
    ind_oper = 0
    operand_full = ['*', '/', '-', '+']
    operands = ['*', '/', '-', '+']
    for op in sech_operand:  # создадим цикл for
        operands.remove(op)
    found = False
    for i, sim in enumerate(exp):
        if i == 0 and sim == '-':
            continue
        if not found and sim in operands:
            ind_start = i + 1
        elif found and sim in operand_full:
            ind_finish = i - 1
            return ind_start, ind_finish, ind_oper
        elif sim in sech_operand:
            found = True
            ind_oper = i
            ind_finish = len(exp) - 1  # len возвращает только целое число
    return ind_start, ind_finish, ind_oper
# рекурсивная функция


def calk(exp):  # которая будет принимать наше выражение
    if '*' in exp or '/' in exp:
        ind_s, ind_f,  ind_o = find(exp, ['*', '/'])
        if exp[ind_o] == '*':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) *
                                     float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calk(exp)
        elif exp[ind_o] == '/':
            exp = exp[0: ind_s] + str(float(exp[ind_s:ind_o]) /
                                      float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calk(exp)

    if '+' in exp or '-' in exp:
        ind_s, ind_f, ind_o = find(exp, ['+', '-'])
        if exp[ind_o] == '+':
            exp = exp[0: ind_s] + str(float(exp[ind_s:ind_o]) +
                                      float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calk(exp)
        elif exp[ind_o] == '-':
            exp = exp[0: ind_s] + str(float(exp[ind_s:ind_o]) -
                                      float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calk(exp)
    return exp


if __name__ == '__main__':
    exp = "4/2*3"
    print(calk(exp))

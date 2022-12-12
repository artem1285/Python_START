"""
Напишите игру "Крестики-нолики".
"""
from random import randint
#  создаем Ф вывода доски
# будет принимать список не более 9 значений типа list


def print_board(array:[list]):
    print('|', end=' ')
    # создадим координаты, нумеруем столбцы
    print(*range(len(array)), sep=' | ', end=' | \n')
    # теперь их надо отобразить друг под другом
    print('-'*13)  # горизонтальные линии
    # enumerate Ф дает индекс и сам элемент. Она возвращает кортеж в кототрм на первом месте индекс I, потом сам элемент/
    for i, line in enumerate(array):
       # i это будет номером строки

        print('|', end=' ')  # черточка в начале и конце
        # распакуем с помощью *.  Надо нарисовать поле - границы. Добавить символ | с помощью sep
        print(*line, sep=' | ', end=f' | {i}\n')
        print('-'*13)
# проверка кто выиграл


def check(array, player):
    if array[0][0] == array[0][1] == array[0][2] != ' ' or array[1][0] == array[1][1] == array[1][2] != ' ' or array[2][0] == array[2][1] == array[2][2] != ' ':
        return True
    if array[0][0] == array[1][0] == array[2][0] != ' ' or array[0][1] == array[1][1] == array[2][1] != ' ' or array[0][2] == array[1][2] == array[2][2] != ' ':
        return True
    if array[0][0] == array[1][1] == array[2][2] != ' ' or array[2][0] == array[1][1] == array[0][2] != ' ':
        return True


if __name__ == '__main__':
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # список списков
    # ход
    print('Начинаем игру крестики/нолики:')
    players = ['0', 'X']
    turn = randint(0, 1)
    player = players[turn]
    print_board(lst)
    while True:
     # запрашиваем куда ставить player
        print(f'Ходит {player}')
        row, col = [int(i) for i in input(
            'Укажите строку и столбец через пробел ').split()]  # в эти переменные row, col
    # запишутся числа
        lst[row][col] = player
        print_board(lst)
        if not check(lst, player):
            turn = not turn
   # делаем смену хода
            player = players[turn]
        else:
            print(f'Подбедили {player}')
            break

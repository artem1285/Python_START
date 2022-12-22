import view
from logger import log
import model
import request


@log
def start():
    """Стартовая функция"""
    view.greetings() # из файла view выдаем приветствие. это print('\n**Справочник студентов ВУЗА**')
    conn, cursor = model.connect() # из model.connect получаем conn, cursor
    while True:# бесконечный цикл, которы выводит меню, когда выходим из нее , при вводе 0, в конце вызываем Ф disconnect, где закрываем соединение с базой
        view.menu() # тут вызываем меню из файла  view - def menu():
        match request.get_command(): # из файла request вызываем get_command - выводится """Запрос команды из меню"""
            case "0":  # если будет 0, то выходим из бесконечного цикла
                break
#  и через операторы match, case какую цифру мы ввели
            case "1":  # если 1 это запрос данных
                view.print_data(model.get_data(cursor)) # обращаемся к Ф get_data и передаем cursor, который находится в Ф model
# в нем через метод execute, в месте def get_data(cursor): посылаем SQL запрос, где соединяются те таблицы, которые есть
            case "2":  # Добавить новую запись. Запрашиваем все данные, кроме ID и номер терефона, который добавляем отделным списком
                data = request.get_data()
                model.add_record(conn, cursor, data)

            case "3":  # Редактировать запись по id
                data = model.get_data_id(cursor, request.get_id()) # запрашиваем номер id, какую запись мы ходим редактировать
                if data: # если такое id есть,   
                    view.print_data(data)  # тогда их показываем
                    new_data = request.get_data() # запрашиваем новые данные 
                    model.edit_data(conn, cursor, data[0][0], new_data) # все это передаем в файл model edit
                else:
                    view.print_error()

            case "4":  # Удалить запись
                model.del_data(conn, cursor, request.get_id()) #  так же запрашиваем что хотим удалить

    model.disconnect(conn)
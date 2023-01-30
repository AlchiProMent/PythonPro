# удаление записей
#
import sqlite3 as sq3

def del_rec(id):
    # подключиться к базе данных
    db_students = sq3.connect('C:\Code\PythonPro\DB\students.db')
    # создать курсор для запросов к БД
    query = db_students.cursor()

    try:
        SQL_DEL = f'DELETE FROM tb_students WHERE id={id}'
        # выполнить запрос
        res = query.execute(SQL_DEL)

    except sq3.OperationalError:
        print('Ошибка при удалениии данных в БД!')
    else:
        # зафиксировать изменения в базе данных
        db_students.commit()
        print(f'Запись удалена. Результат: {res}')
    finally:
        # закрыть соединений с базой данных
        db_students.close()

if __name__ == '__main__':
    id = input('Введите ID удаляемой записи: ')
    del_rec(id)

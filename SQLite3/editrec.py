# редактирование записей
#
# удаление записей
#
import sqlite3 as sq3

def edit_rec(id, new_fc):
    # подключиться к базе данных
    db_students = sq3.connect('..\DB\students.db')
    # создать курсор для запросов к БД
    query = db_students.cursor()

    try:
        # шаблон комнады для редактирования
        SQL_UP = f'UPDATE tb_students SET faculty="{new_fc}" WHERE id={id}'
        # выполнить команду
        res = query.execute(SQL_UP)

    except sq3.OperationalError:
        print('Ошибка при редактировании данных в БД!')
    else:
        # зафиксировать изменения в базе данных
        db_students.commit()
        print(f'Запись успешно обновлена')
    finally:
        # закрыть соединений с базой данных
        db_students.close()

if __name__ == '__main__':
    id = input('Введите ID редактируемой записи: ')
    new_faculty = input('Введите новый факультет: ')
    edit_rec(id, new_faculty)

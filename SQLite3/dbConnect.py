# демонстрация работы с SQLite3
#
import sqlite3 as sq3

# подключиться к базе данных
db_students = sq3.connect('..\DB\students.db')
# создать курсор для запросов к БД
query = db_students.cursor()

try:
    # выполнить запрос
    res_query = query.execute('SELECT * FROM tb_students ORDER BY id')
except sq3.OperationalError:
    print('Ошибка при запросе к БД!')
else:
    # вывести полученные данные
    for tpl in res_query:
        print(tpl)
finally:
    # закрыть соединений с базой данных
    db_students.close()

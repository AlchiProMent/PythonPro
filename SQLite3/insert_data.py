# демонстрация работы с SQLite3
#
import sqlite3 as sq3

# подключиться к базе данных
db_students = sq3.connect('C:\Code\PythonPro\DB\students.db')
# создать курсор для запросов к БД
query = db_students.cursor()

try:
    # выполнить запрос
    # res_query = query.execute('INSERT INTO tb_students (id,fio,city,faculty,campus,address) VALUES (9,"Ефремова И.Н.","Москва","ФИТ","","")')
    recs = ((27, "Найденкова Д.М.", "Иваново", "ФИТ", "Корпус 2", "ул.Чипполино, 45"),
            (28, "Овсиенко И.П.", "Нижний Новгород", "ФПА", "Корпус 1", "ул.Синеухова, 23"),
            (29, "Пашкаев Ю.Б.", "Чита", "ФИТ", "Корпус 2", "ул.Чипполино, 45"),
            (30, "Потапова В.В.", "Москва", "ФИТ", "", ""),
            (31, "Салимов Р.Н.", "Казань", "ФИТ", "Корпус 2", "ул.Чипполино, 45"),
            (32, "Сорокин Д.К.", "Санкт-Петерубрг", "ФПА", "Корпус 1", "ул.Синеухова, 23"))

    # добавить несколько записей
    query.executemany('INSERT INTO tb_students (id,fio,city,faculty,campus,address) VALUES (?,?,?,?,?,?)', recs)

except sq3.OperationalError:
    print('Ошибка при добавлении данных в БД!')
else:
    # зафиксировать изменения в базе данных
    db_students.commit()
    print('Успешное добавление.')
finally:
    # закрыть соединений с базой данных
    db_students.close()

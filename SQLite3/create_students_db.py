# создание таблиц базы данных "студенты"
#
import sqlite3
import pandas as pnd

DATABASE_NAME = 'C:/Code/PythonPro/DB/students.db'
SCRIPT_NAME = 'C:\Code\PythonPro\SQLite3\create_db.sql'
EXCEL_NAME = 'C:/Code/PythonPro/Excel/список.xlsx'
SHEET_NAME = 'Студенты 2'

def load_script(script_name):
    # загрузить скрипт из файла и вернуть его
    script = ''
    try:
        with open(script_name, encoding='utf-8') as f:
            script = f.read()
    except FileNotFoundError:
        print(f'Файл "{script_name}" не найден.')
    except:
        print(f'Ошибка чтения скрипта "{script_name}"')
    return script


def exec_script(conn, script):
    # выполнить скрипт

    # создать курсор
    cursor = conn.cursor()
    try:
        cursor.executescript(script)
    except sqlite3.Error as err:
        print(f'Ошибка запуска скрипта: {err}')
        return False
    else:
        conn.commit()
        return True


def insert_students(conn, excel_file_name):
    # парсинг и добавление данных в таблицу
    try:
        df = pnd.ExcelFile(excel_file_name)
    except:
        print(f'Ошибка чтения файла "{excel_file_name}"')
    else:
        # получить лист с именем SHEET_NAME
        sheet = df.parse(SHEET_NAME)
        # получить табличные данные
        table = sheet.values
        # список для кортежей сохраняемых значений
        students = []
        # цикл по строкам
        for row in table:
            # добавить очередной кортеж
            students.append( (row[0], row[1], row[2], row[3], row[4]+1) )

        cursor = conn.cursor()
        try:
            cursor.executemany('INSERT INTO o_students VALUES (?,?,?,?,?)', students)
        except:
            print('Ошибка при попытке добавить студентов!')
        else:
            conn.commit()
            print('Группа студентов сохранена в базу данных.')


def create_database(db_name):
    # функция для полного цикла создания всех таблиц базы данных
    if (scr := load_script(SCRIPT_NAME)):
        # подключить базу данных
        try:
            db = sqlite3.connect(db_name)
        except sqlite3.Error as err:
            print(f'Ошибка при подключении к базе данных [{db_name}]: {err}')
        else:
            # выполнить скрипт
            if exec_script(db, scr):
                # если скрипт выполнился - добавить данные о студентах
                insert_students(db, EXCEL_NAME)
        finally:
            # закрыть БД
            db.close()
    else:
        print('Не удалось загрузить SQL-скрипт!')
    print('Программа завершена.')

if __name__ == '__main__':
    create_database(DATABASE_NAME)
# работа с CSV-файлом
#
import pandas as pnd

# имя файла
CSV_NAME = 'cities.csv'


def make_csv(file_name):
    # создание CSV-файла
    df_cities = pnd.DataFrame({'city': ['Москва', 'Санкт-Петербург', 'Владимир', 'Рязань', 'Новгород','Смоленск','Курск'],
                               'area': [2561, 1439, 137, 224, 90,166,208],
                               'population': [13000, 5600, 349, 528, 224,316,440]})
    try:
        df_cities.to_csv(file_name, index=False)
    except:
        print('Ошибка при сохранении данных!')
    else:
        print(f'Данные успешно сохранены в файл "{file_name}"')


def read_csv_file(file_name):
    # чтение CSV-файла
    try:
        df = pnd.read_csv(file_name)
    except FileNotFoundError:
        print(f'Файл "{file_name}" не найден!')
    except:
        print(f'Ошибка при чтении файла "{file_name}"')
    else:
        # получить данные в виде таблицы
        table = df.values
        # вывести их на консоль
        for row in table:
            for cell in row:
                print(cell, end=' | ')
            print()

if __name__ == '__main__':
    make_csv(CSV_NAME)
    read_csv_file(CSV_NAME)
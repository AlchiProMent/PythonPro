# пример разведочного анализа данных
# источник данных: DB\police_killings.csv
import numpy as np
import pandas as pd
import plotly.express as ex

# имя файла для анализа
CSV_FILE = '../DB/police_killings.csv'
# имя файла для сохранения диаграммы
HTML_FILE = 'graph.html'


def csv_load(file_name):
    # загрузить данные из файла
    try:
        data = pd.read_csv(file_name)
    except FileNotFoundError:
        print(f'Файл "{file_name}" не найден!')
        return None
    except:
        print('Ошибка загрузки данных из файла!')
        return None
    else:
        print('Данные успешно загружены.')
        return data

def primary_analysis(df, show_df=False, show_cols=False, show_null_summ=False):
    # первичный анализ датасета
    if show_df:
        print(df)
        print()

    # посмотреть список столбцов
    if show_cols:
        print('Структура данных:')
        print(df.info())

    if show_null_summ:
        print('\nПропущенные значения:')
        print(df.isnull().sum())

    # восполнить численные данные средним по столбцам
    df.fillna(df.mean(), inplace=True)

    # воспольнить остальные значения
    df.fillna('Unkn', inplace=True)

    if show_null_summ:
        print('\nПропущенные значения после преобразования:')
        print(df.isnull().sum())

    # проверка дубликатов
    if duplicates_available(df):
        # удалить дупликаты
        df.drop_duplicates()
    else:
        print('Дупликатов в массиве нет')

def duplicates_available(df):
    # дупликаты имеются?

    # получить массив значение Bool
    dup_bool = df.duplicated()
    # возвращает True, если выборка имеет хотя бы один элемент
    return len(dup_bool[dup_bool != False]) > 0

def show_bar(df, col_name):
    # создание столбчатой диаграммы
    fig = ex.bar(df, x=col_name)
    # вывод в браузере
    fig.write_html(HTML_FILE, auto_open=True)

def show_pie(df, filterable_col, value, col_name):
    # создание столбчатой диаграммы
    fig = ex.pie(df[df[filterable_col]==value], names=col_name)
    # вывод в браузере
    fig.write_html(HTML_FILE, auto_open=True)

def group_research(df):
    # запрашивать названия столбцов
    while (col_name := input('Имя столбца для группировки: ')) != '':
        if col_name != '':
            # вывод графика
            show_bar(df, col_name)

def group_structure(df):
    # структура группа
    while (f_col := input('Имя столбца для фильтра: ')) != '':
        if f_col != '':
            val = input('Значение фильтра : ')
            col_name = input('Столбец с подгруппами: ')
            # вывод графика
            show_pie(df, f_col, val, col_name)

def go_eda(file_name):
    # загрузить данные из файла
    pk_df = csv_load(file_name)
    # выполнить первичную проверку
    primary_analysis(pk_df)
    # исследование групп
    group_research(pk_df)
    # структура группа
    group_structure(pk_df)

    # график зависимости возраста убитого и размера дохода домохозяйства района
    pk_df.sort_values(by='age', inplace=True)
    fig = ex.scatter(pk_df, x='h_income', y='age', color='raceethnicity', size='urate')
    fig.write_html(HTML_FILE, auto_open=True)

if __name__ == '__main__':
    # выполнить развеодчный анализ
    go_eda(CSV_FILE)
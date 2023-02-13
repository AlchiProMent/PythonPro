# восполнение пропущенных значений
import pandas as pd
from pandas import DataFrame
from numpy import nan as NA
from numpy import random

def new_df():
    # создать двумерный массив случайных чисел
    df = DataFrame(random.randint(-100, 100, 60).reshape(12, 5), columns=list('ABCDE'))
    # очистить строки 2, 7 и 10
    df.iloc[[2, 7, 10]] = NA
    # очистить некоторые ячейки
    df.iloc[5, 2] = NA
    df.iloc[0, 1] = NA
    df.iloc[8, 4] = NA
    df.iloc[0, 1] = NA
    df.iloc[11, 0] = NA
    return df

if __name__ == '__main__':
    df = new_df()
    print(df)
    # восполнение нулём
    print(df.fillna(0))

    print()
    df2 = new_df()
    # восполнение по столбцам
    print(df2.fillna({'A': 1111, 'B': 2222, 'C': 3333, 'D': 4444, 'E': 5555}))
    print(df2)
    # изменение массива
    df2.fillna({'A': 1111, 'B': 2222, 'C': 3333, 'D': 4444, 'E': 5555}, inplace=True)
    print(df2)
    print(df)
    # очистить значения
    df.iloc[7:, 0] = NA
    print(df)

    # интерполяция
    print(df.fillna(method='ffill'))
    # интерполяция ограниченного числа элементов
    print(df.fillna(method='ffill', limit=2))
    print()

    # средние значения
    print(df.mean())
    # восполнение средним
    print(df.fillna(df.mean()))

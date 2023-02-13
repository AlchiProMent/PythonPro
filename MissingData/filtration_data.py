# фильтрация отсутствующих данных
import pandas as pd
from pandas import DataFrame
from numpy import nan as NA
from numpy import random

# создать набор данных
ser = pd.Series([11, 22, 33, NA, 55, NA, 77])
print(ser)
print()

# удалить значение элемента
ser[1] = None
print(ser)

print(ser.isnull())
print(ser.notnull())

# фильтрация отсутствующих данных
print(ser[ser.notnull()])

# получить значения
print(ser.dropna())
print()

# создать двумерный массив случайных чисел
df = DataFrame(random.randint(-100, 100, 60).reshape(12, 5), columns=list('ABCDE'))
print(df)

# очистить строки 2, 7 и 10
df.iloc[ [2, 7, 10] ] = NA
print(df)
print()

# очистить некоторые ячейки
df.iloc[5, 2] = NA
df.iloc[0, 1] = NA
df.iloc[8, 4] = NA
df.iloc[0, 1] = NA
df.iloc[11, 0] = NA
print(df)

print()
# выдать только полные строки
print(df.dropna())

print()
# отбросить только пустые строки
print(df.dropna(how='all'))

print()
# отбросить столбцы с NA
print(df.dropna(axis=1))

# ввести произвольное значение в столбцы A и D
df[['A', 'D']] = 123
print(df)

print()
# отбросить столбцы с NA
print(df.dropna(axis=1))

# очистить столбец C
df['C'] = NA
print(df)

print()
# отбросить столбцы с NA
print(df.dropna(axis=1, how='all'))

print()
print(df)
# выполнить "тонкую настройку"
print(df.dropna(thresh=4))
print(df.dropna(thresh=3))
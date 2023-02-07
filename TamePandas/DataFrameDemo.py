# работа с объектом класса DataFrame
import pandas as pd
from pandas import DataFrame

# словарь с описанием фильмов
harry_potter_movies = {'Movie': ['Philosophers Stone',
                                 'Chamber of Secrets',
                                 'Prisoner of Azkaban',
                                 'Goblet of Fire',
                                 'Order of the Phoenix'],
                       'Released': [2001, 2002, 2004, 2005, 2007],
                       'Budget': [125_000_000, 100_000_000, 130_000_000, 150_000_000, 150_000_000],
                       'Duration': [125, 174, 142, 157, 138]}

# создать объект на основе словаря
hpm_df = DataFrame(harry_potter_movies)
print(hpm_df)
print()

# создать объект с другим порядком столбцов
hpm2 = DataFrame(harry_potter_movies, columns=['Movie','Duration','Budget','Released'])
print(hpm2)
print()

# установить новые индексы
hpm3 = DataFrame(harry_potter_movies, index=['PS', 'CS', 'PA', 'GF', 'OP'])
print(hpm3)
print()

# дополнительная колонка
hpm4 = DataFrame(harry_potter_movies,
                 columns=['Movie','Duration','Budget','Released', 'Producer'],
                 index=['PS', 'CS', 'PA', 'GF', 'OP'])
print(hpm4)
print()

# извлечь столбец
print(hpm4['Movie'])
print(hpm4.Duration)
print()

# список индексов
print(hpm4.columns)

# добавить значение в столбец
hpm4['Producer'] = 'David Heyman'
print(hpm4)
print()

# присваивание через список
hpm5 = DataFrame(harry_potter_movies,
                 columns=['Movie','Duration','Budget','Released', 'Fees'])
print(hpm5)
hpm5['fees'] = [1000_000_000, 879_000_000, 797_000_000, 897_000_000, 940_000_000]
print(hpm5)
print()

# добавить столбец
hpm5['Producer'] = 'David Heyman'
print(hpm5)
print()

# присваивание значений при помощи Series
imdb_ratings = pd.Series([7.6, 7.9, 7.5], index=['PS', 'PA', 'OP'])
hpm4['imdb'] = imdb_ratings
print(hpm4)
# удалить столбец
del hpm4['imdb']
print(hpm4)
print()

# создание через словарь словарей
profit_and_loss = {'Profit': {2021: 450.43, 2022: 789.91},
                   'Loss': {2020: 376.11, 2021: 402.18, 2022: 634.55}}
pal_df = DataFrame(profit_and_loss)
print(pal_df)
print()
# транспонирование
print(pal_df.T)
print()

pal_df.index.name = 'Years'
pal_df.columns.name = 'Items'
print(pal_df)
print()

# вывод таблицы
print(hpm4.values)
# Индексные объекты
import pandas as pd
from pandas import Series, DataFrame

# создать простой объект
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])
print(index[1])

# это ошибка:
# index[1] = 'd'

# создать индексный объект
ind = pd.Index(range(1,5))
obj2 = Series([21,22,23,24], index=ind)
print(obj2)
print(obj2.index)
# создать второй объект с тем же индексом
obj3 = Series([31,32,33,34], index=ind)
print(obj3)
print(obj3.index)
# сложить значения объектов
print(obj2 + obj3)
print()

# создание через словарь словарей
profit_and_loss = {'Profit': {2021: 450.43, 2022: 789.91},
                   'Loss': {2020: 376.11, 2021: 402.18, 2022: 634.55}}
pal_df = DataFrame(profit_and_loss)
pal_df.index.name = 'Years'
pal_df.columns.name = 'Items'
print(pal_df)

# проверить наличие индексов
print(2021 in pal_df.index)
print(2019 in pal_df.index)
print()
print('Profit' in pal_df.columns)
print('Looser' in pal_df.columns)
print()

# переиндексация
obj3 = Series([11,12,13,14], ['a', 'b', 'c', 'd'])
print(obj3)
obj4 = obj3.reindex(['d', 'c', 'b', 'a', 'e'])
print(obj4)
print()

# переиндексация DataFrame
print(pal_df)
pal2 = pal_df.reindex([2019, 2020, 2021, 2022])
print(pal2)
# переиндексация по столбцам
pal3 = pal_df.reindex(columns=['Loss', 'Profit', 'Flow'])
print(pal3)
print()

# удаление по осям
pal4 = pal2.drop([2019, 2021])
print(pal4)
print()

pal5 = pal3.drop(['Loss', 'Flow'], axis=1)
print(pal5)
print()

# доступ по индексам
print(obj3['a'], obj4['d'])
print(obj4)
print(obj4['b':'e'])
print()

# обращение с использованием loc и iloc
print(pal3)
print()
print(pal3.loc[2021,'Profit'])
print(pal3.loc[2021,['Flow','Profit']])
print(pal3.loc[[2021,2020],['Flow','Profit']])
print()

print(pal3.iloc[[0,1],[0,2]])
# введение в работу с классом Series
import numpy as np
import pandas as pd
from pandas import Series

# простейший объект Series
ser1 = Series([100, 200, 300, 400])
print(ser1)

# объект Series с индексами
ser2 = Series([100, 200, 300, 400], index=['A', 'B', 'C', 'D'])
print(ser2)

# просмотреть индексы
print(ser2.index)

# получить доступ к элементам по индексу
print(ser2['D'], ser2['B'])

# произвольная выборка по индексам
print(ser2[['C', 'D', 'A']])

# использование булевых индексов
print(ser2[ser2 > 200])

# сложное условие выборки
print(ser2[(ser2 > 100) & (ser2 < 400)])

# поделить все элементы на 10
print(ser2 / 10)

# экспонента
print(np.exp(ser2))

# проверка принадлежности индекса
print('B' in ser2)
print('X' in ser2)

# создание объекта из словаря
cities = {'Moscow': 13.09, 'Pekin': 21.89, 'Delhi': 9.88, 'Rome': 2.75, 'Istanbul': 15.03}
cobj = Series(cities)
print(cobj)

# создание нового объекта на основе существующего
cities_names = ['Moscow', 'Pekin', 'Paris', 'Rome']
cobj2 = Series(cobj, index=cities_names)
print(cobj2)

# проверка отсутствующих значений
print(pd.isnull(cobj2))
print(pd.notnull(cobj2))
print()
print(cobj2.isnull())
print(cobj2.notnull())

# выравнивание при математических операциях
print()
print(cobj + cobj2)

cobj2.name = 'Cities'
cobj2.index.name = 'City'
print(cobj2)
print()

# изменение индексов объекта
print(ser1)
ser1.index = ['zero', 'one', 'two', 'three']
print(ser1)




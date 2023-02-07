# операции над массивами
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# создать массивы
a1 = pd.Series([10, 20, 30, 40], index=['A', 'C', 'D', 'E'])
a2 = pd.Series([1, 2, 3, 4, 5], index=['A', 'C', 'E', 'F', 'G'])
print(a1)
print(a2)
# сложить массивы
print(a1 + a2)
print()

# создать массивы DataFrame
df1 = DataFrame(np.arange(9).reshape((3, 3)), columns=list('BCD'), index=['one', 'two', 'three'])
print(df1)
df2 = DataFrame(np.arange(12).reshape((4, 3)), columns=list('BDE'), index=['one', 'two', 'three', 'four'])
print(df2)
# сложить два массива и вывести результат
print(df1 + df2)
print()

# сложение объектов с непересекающимися индексами
df3 = DataFrame({'A': [1, 2]})
df4 = DataFrame({'B': [3, 4]})
print(df3 + df4)
print()

# восполнение значений
print(df1.add(df2, fill_value=0))
print()
# вычитание
print(df1.sub(df2, fill_value=0))
print()
# деление
print(df1.div(df2, fill_value=1))
print()
# деление с отсечением
print(df1.floordiv(df2, fill_value=1))
print()
# умножение
print(df1.mul(df2, fill_value=1))
print()
# возведение в степень
print(df1.pow(df2, fill_value=1))
print()

# укладывание
sobj = Series([2, 3, 4], index=['B', 'D', 'E'])
print(sobj)
print(df2)
print(df2 - sobj)
print()
print(df1)
print()
print(df1 - sobj)
print()

# операция над столбцами
sobj2 = Series([10, 11, 12], index=['one', 'two', 'four'])
print(sobj2)
print(df2.sub(sobj2, axis='index'))
print()

# создать массив
df = DataFrame(np.arange(12).reshape((3, 4)), index=['Beta', 'Zero', 'Alfa'], columns=list('DABF'))
print(df)
print(df.sort_index())
print(df.sort_index(axis=1))
print(df.sort_index(axis=1, ascending=False))
print()

# сортировка по значениям
unsort_df = DataFrame(np.random.randn(12).reshape((4, 3)), columns=list('ABC'))
print(unsort_df)
print(unsort_df.sort_values(by='B'))
print(unsort_df.sort_values(by=['B', 'C']))
print()
newcol = Series([2, 1, 2, 1])
unsort_df['B'] = newcol
print(unsort_df.sort_values(by=['B', 'C']))
print()

# повторяющиеся индексы
so = Series([2, 5, 2, 67, 12, -8, 3], index=['A', 'A', 'B', 'B', 'B', 'C', 'D'])
print(so)
print(so['C'])
print(so['B'])
print()

ddf = DataFrame(np.random.randn(15).reshape((5, 3)), index=list('AABBC'))
print(ddf)
print(ddf.loc['A'])
print()

# нет дублей
print(df1.index.is_unique)
# есть дубли
print(ddf.index.is_unique)




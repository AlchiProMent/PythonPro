# простые методы борьбы с пропущенными данными
import pandas as pd
import numpy as np
from pandas import DataFrame

# график дневных измерений температуры
temp = {'20':[37.9, 37.1, np.nan, 37.5, np.nan, 37.1],
        '21':[37.2, np.nan, 38.5, 37.5, 38.5, 37.0],
        '22':[36.6, 37.5, 38.0, np.nan, 37.5, 36.8]}
# индексы
names = pd.Index(['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров'])
# больные
sicks = DataFrame(temp, index=names)
print(sicks)

# найти среднее по палате
print('\nСреднее по палате:')
print(sicks.mean())

# найти среднее по палате
print('\nСреднее по больному:')
print(sicks.mean(axis=1, skipna=False))

print('\nСумма по столбцам:')
print(sicks.sum())

print('\nСумма по строкам:')
print(sicks.sum(axis=1))

print('\nСтандартное отклонение:')
print(sicks.std())

print('\nДисперсия:')
print(sicks.var())

print('\nМедиана:')
print(sicks.median())

print('\nКвантиль 0.25:')
print(sicks.quantile(0.25))

print('\nКвантиль 0.75:')
print(sicks.quantile(0.75))

#print('\nСреднее отклонение от среднего:')
#print(sicks.mad())

print('\nСреднее отклонение от среднего (расчётное):')
print((sicks - sicks.mean()).abs().mean())

print('\nАссиметрия:')
print(sicks.skew())

print('\nКуртозис:')
print(sicks.kurt())

print('\nНарастающая сумма:')
print(sicks.cumsum())

print('\nНарастающее произведение:')
print(sicks.cumprod())

print('\nНарастающий минимум:')
print(sicks.cummin())

print('\nНарастающий максимум:')
print(sicks.cummax())

print('\nПервая арифметическая разность:')
print(sicks.diff())

print('\nПроцентное изменение:')
print(sicks.pct_change())

print('\nПроцентное изменение (по больным):')
print(sicks.pct_change(axis=1))

print('\nСводные статистики:')
print(sicks.describe())

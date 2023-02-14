# демонстрация графиков Plot
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame

# создать основу для 3 диаграмм
fg, ax = plt.subplots(ncols=3, figsize=(18, 5), width_ratios=[6, 4, 4])

# 1-я диаграмма #################################

# нормально распределенная последователоность из 100 чисел
x = np.linspace(0, 10, 100)
# F(x)
f = lambda x: 4 + 2 * np.sin(2 * x)

# построить график
ax[0].plot(x, f(x))
# задать оси
ax[0].set_xlim([0, 10])
ax[0].set_ylim([0, 7])
ax[0].set_title('График 2Sin(2x)+4')
ax[0].grid()

# аннотации
ax[0].annotate('См.здесь', xy=(5.5,2), xytext=(3, 1), arrowprops=dict(facecolor='blue', arrowstyle='-|>'))
ax[0].scatter([5.5],[2.05], color='red')

# 2-я диаграмма #################################

# массив данных
ser = Series([5, 7, 20, 23, 44, 51, 15, 22], index=[10, 20, 30, 40, 50, 60, 70, 80])
ax[1].plot(ser, marker='o', ms=10, mfc='#7ad686', mec='#e66f3c')
ax[1].grid(axis='y', color='#dddddd', linestyle='dashed')
ax[1].tick_params(left=False)
ax[1].set_xlim([0, 100])
ax[1].set_ylim([0, 60])
ax[1].set_title('Массив Series')

# 3-я диаграмма #################################
df = DataFrame([[5, 7, 20, 23],
                [23, 49, 40, 23],
                [44, 51, 15, 22],
                [10, 10, 10, 10],
                [45, 89, 37, 100],
                [25, 110, 30, 100]], columns=['Иголки','Булавки','Кнопки','Скрепки'])

ax[2].plot(df, label=df.columns)
ax[2].legend(title='Продукция', ncols=2)
ax[2].set_title('Выпуск продукции иголочной фабрики')
ax[2].grid(axis='x')
ax[2].tick_params(bottom=False)

# компактное размещение
plt.tight_layout()
plt.show()

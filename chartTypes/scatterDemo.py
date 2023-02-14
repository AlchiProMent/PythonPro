# примеры использования точечных диаграмм
import matplotlib.pyplot as plt
import numpy as np

# создать объекты
fg, ax = plt.subplots(figsize=(14, 6), ncols=2)

# массивы данных
x = np.array([23])
y = np.array([48])

rgba = np.array([7, 6, 9, 2])/10
# нарисовать график
ax[0].scatter(x, y, s=2500, color=rgba, edgecolors='black', linewidths=3, alpha=.7)

# установить значения для осей
ax[0].set_xlim([0, 40])
ax[0].set_ylim([0, 60])

# вывести сетку
ax[0].grid(color='#dddddd')
# убрать сетку на задний план
ax[0].set_axisbelow(True)

# плотность веросятности нормального распределения
tot_elements = 54
x = 4 + np.random.normal(0, 2, tot_elements)
y = 4 + np.random.normal(0, 2, tot_elements)
# формирование выборок с равномерным распределением вероятностей для размера и цвета
sizes = np.random.uniform(15, 1800, tot_elements)
colors = np.random.uniform(15, 80, tot_elements)

# нарисовать правую диаграму
ax[1].scatter(x, y, s=sizes, c=colors, alpha=0.5)

plt.show()
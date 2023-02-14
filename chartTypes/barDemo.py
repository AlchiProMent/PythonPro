# столбчатые диаграммы и гистограмма
import matplotlib.pyplot as plt
import numpy as np

# создать фигуру для диаграмм
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# создать массивы
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

# нарисовать диаграмму
ax[0, 0].bar(x, y, width=.8, color='#2896d7')
# настроить оси
ax[0, 0].set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 7.5), yticks=np.arange(1, 8))

# года
years = ['2019', '2020', '2021', '2022']
# объёмы выручки
counts = [40, 100, 30, 55]
# названия столбиков
bar_labels = ['худшие', 'лучшие', '_худшие', 'средние']
# цвета столбиков
bar_color = ['tab:red', 'tab:green', 'tab:red', 'tab:orange']

ax[0, 1].bar(years, counts, label=bar_labels, color=bar_color)
ax[0, 1].legend(title='Объёмы')

ax[0, 1].set_ylabel('Выручка (млн руб.)')
ax[0, 1].set_title('Объемы продаж по годам')
ax[0, 1].grid(axis='y')
ax[0, 1].set_axisbelow(True)

# диаграмма сравнения показателей двух команд
labels = ['Волейбол', 'Баскетбол', 'Теннис', 'Бег', 'Марафон']
our_teams = [20, 34, 30, 35, 27]
visiting_teams = [25, 32, 34, 20, 25]

x = np.arange(len(labels))
# ширина бара
width = 0.35

# вывести бары
rects1 = ax[1, 0].bar(x - width / 2, our_teams, width, label='Наши')
rects2 = ax[1, 0].bar(x + width / 2, visiting_teams, width, label='Гости')

# вывеси подписи
ax[1, 0].bar_label(rects1, padding=-16, color='white')
ax[1, 0].bar_label(rects2, padding=-16)
ax[1, 0].legend(title='Команды')
ax[1, 0].set_title('Дружеские соревнования')
ax[1, 0].set_ylabel('Очки')
ax[1, 0].set_xticks(x, labels)

# гистограмма распределения IQ

# среднее распределение (мю)
mu = 100
# стандартное отклонение (сигма)
sigma = 15
# рассчитать массив случайных значений
x = mu + sigma * np.random.randn(450)

ax[1, 1].hist(x, bins=40)
ax[1, 1].set_xlabel('Уровень IQ')
ax[1, 1].set_ylabel('Плотность вероятности')
ax[1, 1].set_title('Гистограмма оценок IQ: $\mu=100$, $\sigma=15$')

# вывести окно
plt.show()
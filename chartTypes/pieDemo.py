# круговая диаграмма
import matplotlib.pyplot as plt

data = [25, 14, 32, 45, 18]
titles = ['Телевизоры', 'Компьютеры', 'Планшеты', 'Смартфоны', 'Фотоаппараты']
fg = plt.figure('Круговая диаграмма', figsize=(12, 8))
ax = fg.add_subplot(1, 1, 1)
colors = ['#59f751', '#65d2e2', '#f59ef8', '#f2c791', '#afafd3']
# нарисовать круговую диаграмму
ax.pie(data, autopct='%.0f%%', labels=titles, explode=[0, 0, 0, 0.1, 0], wedgeprops=dict(width=0.5), colors=colors)
ax.legend(bbox_to_anchor=(.1, 1.), title='Виды продукции', ncols=2, frameon=False)
plt.title('Структура продаж в магазине')

plt.show()
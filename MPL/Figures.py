# Изучение объекта figure
import matplotlib.pyplot as plt
import numpy as np

# данные для графиков
data = np.array([1, 2, 3, 4, 5, 6])
data2 = np.array([1, 20, 30])
x = np.arange(0, 100, 10)
y = np.array(np.random.randint(1, 25, 10))

# создать фигуру
fg = plt.figure('График', figsize=(14, 7), facecolor='#ebcaa3')
# создать объекты axes
ax1 = fg.add_subplot(2, 2, 1)
ax2 = fg.add_subplot(2, 2, 2, sharex=ax1, sharey=ax1)
ax3 = fg.add_subplot(2, 2, 3, sharex=ax1)
ax4 = fg.add_subplot(2, 2, 4)
# линейный график
ax1.plot(data)
# график квадратов
ax2.plot(data2**2)
# график кубов
ax3.plot(data2**3, color='#7ad686', marker='o')
# отключить оси 3-й фигуры
#ax3.set_axis_off()

ax4.plot(x, y, color='#808080', ls='--', marker='o', ms=8, mfc='#7ad686', mec='#e66f3c')
# подписи к оси X
ticks = ax4.set_xticks([0, 20, 40, 60, 80])
labels = ax4.set_xticklabels(['ноль', 'двадцать', 'сорок', 'шестьдесят', 'восемьдесят'], rotation=45, fontsize='small')
# включить сетку
ax4.grid()

# plt.subplots_adjust(wspace=0, hspace=0)

# показать окно
plt.show()
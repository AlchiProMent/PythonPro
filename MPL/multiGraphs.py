# несколько графиков в одном окне
import matplotlib.pyplot as plt
import numpy as np
import pylab
# набор данных
data = np.array([0, 2, 4, 6, 8, 10, 12, 14])
# получить фигуру
fig = plt.figure('Три графика', figsize=(8,6))
# создать все axis
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

# сформировать графики
ax1.plot(data, 'b')
ax2.plot(data**2, 'g')
ax3.plot(data**3, 'r')

# вывести окно
plt.show()

# первый простой график
import matplotlib.pyplot as plt
import numpy as np

# набор данных для визуализации
data = np.array([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7])

# создать график
plt.plot(data**3)

# вывести на экран окно с графиком
plt.show()
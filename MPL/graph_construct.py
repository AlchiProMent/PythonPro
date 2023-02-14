# конструирование графиков
import matplotlib.pyplot as plt
import numpy as np

# массив значений x
x = np.arange(-10, 10.1, 0.1)

# задать размер окна
plt.figure(figsize=(16, 8))
# сформировать кривую Sin(x)
plt.plot(x, np.sin(x), 'r', label=r'$f_1(x)=\sin(x)$')
plt.plot(x, np.sin(x), 'g*')
# сформировать кривую Cos(x)
plt.plot(x, np.cos(x), 'b', label=r'$f_2(x)=\cos(x)$')
plt.legend(loc='lower right', fontsize=12)

# Заголовок
plt.title('График Sin(X) и Cos(X)')
plt.text(-10, 0.75, 'Простой график', fontsize=12)
# названия осей
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# вывести сетку
plt.grid()

# вывести окно с графиком
plt.show()

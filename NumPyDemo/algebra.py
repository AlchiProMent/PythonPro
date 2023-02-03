# алгебраические операции над матрицами
import numpy as np
import numpy.linalg as la

# создать два массива случайных чисел
xa = np.random.randint(20, 100, (5, 4))
xy = np.random.randint(70, 150, (5, 4))
print(xa)
print(xy)

# вычислить результат и занести в новый массив
az = np.sqrt(xa ** 2 + xy ** 2)
print('Итоговый массив:\n', az)
print()

# создать совместимые матрицы
ma = np.random.randint(10, 100, (3, 2))
mb = np.random.randint(10, 100, (2, 3))
print(ma)
print(mb)
# выполнить перемножение матрицы
print('Результат умножения матриц:\n', np.dot(ma, mb))
print('Результат умножения матриц:\n', ma.dot(mb))
print()

# создать матрицу 5x5
qm = np.random.randint(10, 1000, (5, 5))
print(qm)
# определитель матрицы
print('Определитель:', la.det(qm))
# обратная матрицы
print('Обратная матрица:\n', la.inv(qm))
print()

# получить диагональ матрицы
print(qm.diagonal())
# одномерный массив
da = np.arange(10)
print('Массив для диагонали:', da)
print('Полученная матрица:\n', np.diag(da))
# сумма диагональных элементов
print(qm)
print('Сумма диагональных элементов:', np.trace(qm))
print()

# массив с дублирующимися значениями
duble_array = np.array([1, 2, 6, 2, 9, 3, 12, 1, 2, 78, 22, 12, 6])
print(np.unique(duble_array))
print(np.sort(duble_array))
print()

print(qm)
print('Сортировка по столбцам:\n', np.sort(qm, axis=0))
print('Сортировка по строкам:\n', np.sort(qm, axis=1))
print()

sa = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sb = np.array([21, 2, 23, 4, 55, 66, 7, 8, 99, 10])
# получить общие элементы
print(np.intersect1d(sa, sb))
# получить элементы, отсутствующие во втором массиве
print(np.setdiff1d(sa, sb))
print()

sarray = np.array(['John','Paul','John','George','Ringo','Ringo'])
# избавиться от повторений
print(np.unique(sarray))
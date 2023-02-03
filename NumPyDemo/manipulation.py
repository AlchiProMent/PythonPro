# манипуляции над массивами
import numpy as np

# создать вектор
arr1 = np.arange(1, 13)
print(arr1)

# изменить размерность
arr2 = arr1.reshape(2, 6)
print(arr2)

# изменить размерность двумерного массива
arr3 = arr2.reshape(3, 4)
print(arr3)

print()
# внести изменение в массив
arr3[2, 1] = 0
print(arr1)
print(arr2)
print(arr3)

# создать трехмерный массив
arr1 = arr1.reshape(3, 2, 2)
print(arr1)
print()

# создать матрицу
m1 = np.arange(20).reshape(5, 4)
print(m1)
print(m1.ravel())
m2 = m1.flatten()
print(m2)

print()
arr10 = np.array([[111,112,113],[121,122,123]])
print('1-й массив:\n',arr10)
arr20 = np.array([[211,212,213],[221,222,223]])
print('2-й массив:\n',arr20)

# объединить массивы в новый
arr30 = np.concatenate([arr10, arr20], axis=0)
print('Итоговый массив:\n',arr30)
arr40 = np.concatenate([arr10, arr20], axis=1)
print('Итоговый массив:\n',arr40)

arr50 = np.vstack((arr10, arr20))
arr60 = np.hstack((arr10, arr20))
print('Вертикальный:\n',arr50)
print('Горизонтальный:\n',arr60)
print()

print(m1)
m11, m12 = np.split(m1,[2])
print('Результат разбиения на два массива:')
print(m11)
print(m12)
m21, m22, m23 = np.split(m1,[1,3])
print('Результат разбиения на три массива:')
print(m21)
print(m22)
print(m23)

mc1, mc2, mc3 = np.split(m1,[1,3], axis=1)
print('Результат разбиения по столбцам:')
print(mc1)
print(mc2)
print(mc3)
print()

# сохранить матрицу m1
np.save('matrix1', m1)
print('Массив сохранен.')
# прочитать массив из файла
new_m1 = np.load('matrix1.npy')
print('Прочитанный массив:\n', new_m1)





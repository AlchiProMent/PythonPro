# операции с массивами NumPy
import numpy as np

lst = list(range(1, 11))
print(lst)
for i, el in enumerate(lst):
    lst[i] = el * 10
print(lst)

# создать простой массив
arr = np.arange(1, 11)
print(arr)
print(arr * 10)
# умножить массив на массив
print(arr * arr)
# возвести в квадрат
print(arr ** 2)
# поделить константу на элменты массива
print(1 / arr)

print()
# сравнение массивов
arr1 = np.array([[1, 2, 5], [8, -2, 18]])
arr2 = np.array([[3, -2, 4], [10, 11, 15]])
print(arr1 > arr2)

print(arr[4])
print(arr[2:5])

arr_slice = arr[3:7]
print(arr_slice)

arr_slice[0] = 100
print(arr_slice)
print(arr)

arr2d = np.array([[11, 12], [21, 22], [31, 32]])
print()
print(arr2d)
print(arr2d[1])
print(arr2d[1, 0])
print(arr2d[1][0])

print(arr2d[0:2])

# квадртаная матрица 4x4
matrix = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]])
print('\nМатрица 4x4:')
print(matrix)
print(matrix[:3, :3])
print(matrix[1:3, 1:3])
# взять второй справа столбец
print(matrix[:, 2:3])
print(matrix[:, :])

# создать матрицу случайных чисел
rand_matrix = np.random.randn(8, 4)
print('\n', rand_matrix)
print('\n', rand_matrix[rand_matrix < 0])
print('\n', rand_matrix[(rand_matrix > 0) & (rand_matrix < 1)])
rand_matrix[rand_matrix < 0] = 0
print('\n', rand_matrix)

print('\n', matrix)
print('\n', matrix[[3, 1]])

matrix2 = np.array( [ [11,12,13,14,15], [21,22,23,24,25], [31,32,33,34,35]] )
print('\n',matrix2)
print('\n',matrix2.T)

asimple = np.array([1,4,9,16,25,36])
print(asimple)
print(np.sqrt(asimple))

a1 = np.array( [4,56,-1,34,12,6,90] )
a2 = np.array( [14,26,21,32,2,5,92] )
print()
# вывести максимальные значения в парах
print(np.maximum(a1, a2))
# первый пример работы с NumPy
import numpy as np

# создать простой одномерный массив
simple_array = np.array([1, 2, 3, 4, 5])
print(simple_array)

# создать двумерный массив
arr2d = np.array([[11, 12, 13], [21, 22, 23]])
print()
print(arr2d)
print('Элемент массива', arr2d[1,2])
print(f'Мерность массива: {arr2d.ndim}; размерность: {arr2d.shape}')

# создание трехмерного массива
arr3d = np.array([arr2d, arr2d])
print()
print(arr3d)
print(f'Мерность массива: {arr3d.ndim}; размерность: {arr3d.shape}')

arrMoreD = np.array( [arr3d, arr3d, arr3d, arr3d] )
print(f'Мерность массива: {arrMoreD.ndim}; размерность: {arrMoreD.shape}')

print('Тип элементов:', arr2d.dtype)

print()
arr_floats = np.array([[1.,2.,3.,4.]])
print(arr_floats)
print('Тип элементов:', arr_floats.dtype)

print()
zero_array = np.zeros(10)
print(zero_array)

print()
zero2d = np.zeros((2,6))
print(zero2d)

print()
zero3d = np.zeros((2,6,3))
print(zero3d)

print()
ones2d = np.ones( (2,5) )
print(ones2d)

print()
empty_arr = np.empty(8)
print(empty_arr)

print()
arr7 = np.full( (2,3), fill_value=7)
print(arr7)

print()
# создание единичной матрицы
identity_matrix = np.eye(5)
print(identity_matrix)

print()
print(np.arange(10))

print()
arr = np.array([1.,2.,3.,4.,5.], dtype=np.float32)
print(arr.dtype)

str_nums = ['-12.5','6','809.23','2.456','11.']
new_arr = np.array(str_nums, dtype=np.float64)
print(new_arr)
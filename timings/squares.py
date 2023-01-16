# измерение времени выполнения операции возведения в квадрат

from LIB.tm import pstopwatch
from funcs import *

# создать список случайных элементов
lst1 = create_random_list(5, 255, 1_000_000)

def q_lst1(lst):
    # возведение в степень через умножение самого на себя
    for ind, el in enumerate(lst):
        lst[ ind ] = el*el
    return lst

def q_lst2(lst):
    # возведение в степень
    for ind, el in enumerate(lst):
        lst[ ind ] = el**2
    return lst

print('Начало работы...')

# выполнить операции и определить время выполнения
t1, lst21 = pstopwatch(q_lst1, lst1, title='Возведение в степень через умножение...')
t2, lst22 = pstopwatch(q_lst2, lst1, title='Возведение в степень через стандартную операцию...')

print('Время выполнения возведения в квадрат:')
print('1. Через умножение: \t{:.12f}'.format(t1))
print('2. Стандартно: \t{:.12f}'.format(t2))

print('Программа закончила выполнение.')

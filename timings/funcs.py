# функции для тестирования
from random import randint
from LIB.tm import stopwatch

def create_random_list(min, max, size):
    # создать список случайных чисел
    return [ randint(min, max) for i in range(size) ]

def sort_list(lst):
    # сортировка списка
    return sorted(lst)

def elements_sum(lst):
    # сумма всех элементов списка
    summa = 0.0
    for n in lst:
        summa += n
    return summa

def el2square(lst):
    # возвезедние в квадрат всех элементов списка
    for index, el in enumerate(lst):
        lst[ index ] = el * el
    return lst

# двоичный поиск в упорядоченном списке
def bin_search(lst, s_element):
    # начальные границы интервала поиска
    left_ind = 0
    right_ind = len(lst) - 1
    # лямбда-функция вычисления текущего индекса
    middle_calc = lambda left, right: (left + right) // 2
    # вычислить начальный индекс для проверки
    index = middle_calc(left_ind, right_ind)

    # поиск в цикле
    while ( lst[index] != s_element ) and ( left_ind < right_ind ):
        if (s_element < lst[index]):
            right_ind = index - 1
        elif (s_element > lst[index]):
            left_ind = index + 1
        # вычислить новый индекс для проверки
        index = middle_calc(left_ind, right_ind)

    # вернуть индекс найденного элемента в случае успеха или минус 1
    return (-1, index)[lst[index] == s_element]

def bubble_search(lst):
    # сортировка методом пузырька
    # запомнить размерность списка
    len_lst = len(lst)
    # внешний цикл
    for i in range(1, len_lst):
        # сканирование списка с конца до i-го элемента
        for j in reversed( range(i, len_lst) ):
            # если левый элемент больше текущего
            if lst[j - 1] > lst[ j ]:
                # надо их поменять местами
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    # вернуть отсортированный массив
    return lst

if __name__ == '__main__':
    # создать список случайных чисел
    t1, lst1 = stopwatch( create_random_list, 12_345, 123_456_789, 100_000 )
    # отсортировать список
    t2, lst2 = stopwatch( sort_list, lst1 )
    # получить сумму всех чисел списка
    t3, summa = stopwatch( elements_sum, lst1 )

    print('\nВремя выполнения операций в секундах:')
    print('-------------------------------------')
    print( 'Создание ста тыс. случайных чисел: \t\t{} сек.'.format(t1) )
    print( 'Сортировка ста тыс. случайных чисел: \t{} сек.'.format(t2) )
    print( 'Суммирование ста тыс. чисел: \t\t\t{} сек.'.format(t3) )






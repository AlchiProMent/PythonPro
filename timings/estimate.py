# оценка сложности при поиске элемента в неупорядоченном списке
from LIB.tm import stopwatch
from funcs import *

# поиск элемента в списке
def el_found(lst, num):
    index = -1
    # последовательный перебор всех элементов массива
    for i, el in enumerate(lst):
        # если найден искомый элемент
        if el == num:
            # запомнить текущий индекс элемента
            index = i
            break
    # вернуть индекс найденного элемента
    return index

# поиск максимального элемента в списке
def max_element(lst):
    element = -1
    for el in lst:
        if el > element:
            element = el
    return element


if __name__ == '__main__':

    print('Начало создания списков...')
    # создать список случайных чисел от 1 до 1000'000 размерностью 100'000
    lst = create_random_list( 1, 1000_000, 100_000 )
    # создать список случайных чисел от 1 до 1000'000 размерностью 1000'000
    lst2 = create_random_list( 1, 1000_000, 1000_000 )
    # создать список случайных чисел от 1 до 1000'000 размерностью 10'000'000
    lst3 = create_random_list( 1, 1000_000, 10_000_000 )

    # создать список случайных чисел от 1 до 10'000'000 размерностью 100'000'000
    lst4 = create_random_list( 1, 10_000_000, 100_000_000 )
    print('Списки созданы.')

    # время поиска 1-го элемента списка
    t1, ind1 = stopwatch( el_found, lst, lst[0] )
    # время поиска последнего элемента списка
    t2, ind2 = stopwatch( el_found, lst, lst[100_000-1] )
    # среднее время поиска
    t3 = (t1 + t2) / 2

    print( 'Наилучшее время: {} (индекс {})'.format(t1,ind1) )
    print( 'Наихудшее время: {} (индекс {})'.format(t2,ind2) )
    print( 'Среднее время: {}'.format(t3) )

    # найти максимальные числа в созданных списках
    t41, max1 = stopwatch( max_element, lst, title='Поиск максимума в 100 тыс...' )
    t42, max2 = stopwatch( max_element, lst2, title='Поиск максимума в миллионе...' )
    t43, max3 = stopwatch( max_element, lst3, title='Поиск максимума в 10 миллионах...' )

    # вывести полученные значения
    print('\n')
    print('Время поиска в ста тысячах элементов: {} (максимальное число: {})'.format(t41,max1))
    print('Время поиска в миллионе элементов: {} (максимальное число: {})'.format(t42,max2))
    print('Время поиска в 10 миллионах элементов: {} (максимальное число: {})'.format(t43,max3))

    t44, max4 = stopwatch( max_element, lst4, title='Поиск максимума в 100 миллионах...' )
    print('Время поиска в 100 миллионах элементов: {} (максимум: {})'.format(t44,max4))
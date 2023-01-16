# логарифмическая сложность: бинарный поиск
from LIB.tm import pstopwatch
from funcs import *

print( 'Создание списков...' )
lst1 = list ( range(10_000) )
lst2 = list ( range(100_000) )
lst3 = list ( range(1000_000) )
lst4 = list ( range(100_000_000) )
print( 'Списки созданы.\n\n' )

# поиск в списках
t1, ind1 = pstopwatch( bin_search, lst1, 567, title='Поиск в 10 тыс. чисел...' )
t2, ind2 = pstopwatch( bin_search, lst2, 5678, title='Поиск в 100 тыс. чисел...' )
t3, ind3 = pstopwatch( bin_search, lst3, 56789, title='Поиск в 1 млн. чисел...' )
t4, ind4 = pstopwatch( bin_search, lst4, 5678987, title='Поиск в 100 млн. чисел...' )

# вывести результат
print( 'Для 10 тыс: \t{:.12f} (индекс {})'.format(t1, ind1) )
print( 'Для 100 тыс: \t{:.12f} (индекс {})'.format(t2, ind2) )
print( 'Для 1 млн: \t{:.12f} (индекс {})'.format(t3, ind3) )
print( 'Для 10 млн: \t{:.12f} (индекс {})'.format(t4, ind4) )



from LIB.tm import stopwatch
from  funcs import *

# создание списков разной величины из случайных чисел
t11, lst1 = stopwatch( create_random_list, 10, 999999, 1000, title='\nСоздание тысячи...' )
t12, lst2 = stopwatch( create_random_list, 10, 999999, 10_000, title='\nСоздание 10 тысяч...' )
t13, lst3 = stopwatch( create_random_list, 10, 999999, 100_000, title='\nСоздание 100 тысяч...' )
t14, lst4 = stopwatch( create_random_list, 10, 999999, 1000_000, title='\nСоздание миллиона...' )
t15, lst5 = stopwatch( create_random_list, 10, 999999, 10_000_000, title='\nСоздание 10 миллионов...' )

# сортировка списков
t21, lst1 = stopwatch( sort_list, lst1, title='\nСортировка тысячи....' )
t22, lst2 = stopwatch( sort_list, lst2, title='\nСортировка 10 тысяч....' )
t23, lst3 = stopwatch( sort_list, lst3, title='\nСортировка 100 тысяч....' )
t24, lst4 = stopwatch( sort_list, lst4, title='\nСортировка миллиона....' )
t25, lst5 = stopwatch( sort_list, lst5, title='\nСортировка 10 миллионов....' )

# суммирование чисел в списках
t31, summa1 = stopwatch( elements_sum, lst1, title='\nСуммирование тысячи...' )
t32, summa2 = stopwatch( elements_sum, lst2, title='\nСуммирование 10 тысяч...' )
t33, summa3 = stopwatch( elements_sum, lst3, title='\nСуммирование 100 тысяч...' )
t34, summa4 = stopwatch( elements_sum, lst4, title='\nСуммирование миллиона...' )
t35, summa5 = stopwatch( elements_sum, lst5, title='\nСуммирование 10 миллионов...' )

# возведение в квадрат всех элементов списков
t41, lst1 = stopwatch( el2square, lst1, title='\nВозведение в квадрат 1000 элементов...' )
t42, lst2 = stopwatch( el2square, lst2, title='\nВозведение в квадрат 10 тыс. элементов...' )
t43, lst3 = stopwatch( el2square, lst3, title='\nВозведение в квадрат 100 тыс. элементов...' )
t44, lst4 = stopwatch( el2square, lst4, title='\nВозведение в квадрат миллиона элементов...' )
t45, lst5 = stopwatch( el2square, lst5, title='\nВозведение в квадрат 10 миллионов элементов...' )

width = 80
underline = '-'*width
print('\n\n')
print('Тайминги операций (сек.)'.center(width))
print(underline)
print('\t\t\t|{:^12,d}|{:^12,d}|{:^12,d}|{:^12,d}|{:^12,d}'.format(1000,10_000,100_000,1000_000,10_000_000))
print(underline)

# тело таблицы
print( 'Создание    |{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}'.format(t11,t12,t13,t14,t15) )
print(underline)
print( 'Сортировка  |{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}'.format(t21,t22,t23,t24,t25) )
print(underline)
print( 'Суммирование|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}'.format(t31,t32,t33,t34,t35) )
print(underline)
print( 'Квадраты    |{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}|{:^12,.6f}'.format(t41,t42,t43,t44,t45) )
print(underline)







# проверка эффективности "пузырьковой сортировки"
from LIB.tm import pstopwatch
from funcs import *

# создание списков
t11, lst1 = pstopwatch(create_random_list, 54_321,  987_654_321, 100, title='\nСоздание списка из 100 элементов...')
t21, lst2 = pstopwatch(create_random_list, 54_321,  987_654_321, 1000, title='\nСоздание списка из 1000 элементов...')
t31, lst3 = pstopwatch(create_random_list, 54_321,  987_654_321, 5000, title='\nСоздание списка из 5000 элементов...')
t41, lst4 = pstopwatch(create_random_list, 54_321,  987_654_321, 10000, title='\nСоздание списка из 10 000 элементов...')
t51, lst5 = pstopwatch(create_random_list, 54_321,  987_654_321, 15000, title='\nСоздание списка из 15 000 элементов...')

# сортировка списков
t12, lst1 = pstopwatch(bubble_search, lst1, title='\nСортировка 100 элементов...')
t22, lst2 = pstopwatch(bubble_search, lst2, title='\nСортировка 1000 элементов...')
t32, lst3 = pstopwatch(bubble_search, lst3, title='\nСортировка 5000 элементов...')
t42, lst4 = pstopwatch(bubble_search, lst4, title='\nСортировка 10 000 элементов...')
t52, lst5 = pstopwatch(bubble_search, lst5, title='\nСортировка 15 000 элементов...')

print('\n\nРезультаты выполнения пузырьковой сортировки:')
print('--------------------------------------------')
print(f'Сортировка 100 элементов: {t12} сек.')
print(f'Сортировка 1000 элементов: {t22} сек.')
print(f'Сортировка 5000 элементов: {t32} сек.')
print(f'Сортировка 10 000 элементов: {t42} сек.')
print(f'Сортировка 15 000 элементов: {t52} сек.')

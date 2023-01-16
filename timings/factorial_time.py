# O(n!) - факториальная сложность
# Задача коммивояжера перебором
#

from LIB.tm import pstopwatch
from numpy import random
from itertools import permutations

def get_matrix(total_points, min, max, show_matrix=False):
    # функция, создающая квадратную матрицу расстояний со случайными числами

    # получить матрицу случайных расстояний между пунктами
    point_paths = random.randint(min, max, (total_points, total_points))
    # обнулить главную даигональ матрицы
    for i in range(total_points):
        point_paths[i][i] = 0
    # установить соответствие строк над главной диагональю и столбцов под ней
    for i in range(total_points):
        for j in range(i, total_points):
            # установить значение ячейки в столбце под диагональю из ячейки строки над диагональю
            point_paths[j][i] = point_paths[i][j]

    # вывести на экран
    if show_matrix:
        print(f'Матрица {total_points}x{total_points} расстояний между точками')
        for row in point_paths:
            print(row)
        print()

    # вернуть полученную матрицу
    return point_paths

def get_shortest_path(matrix, view_path=False):
    # получить кратчайший путь
    # размерность матрицы
    len_matrix = len(matrix)
    # создать первую последовательность в естественном порядке (0,1,2,3,4... и т.д.)
    row_path = list( x for x in range(len_matrix) )
    # сгенерировать все возможные перестановки
    all_paths = list( permutations(row_path, len_matrix) )

    # начальное значение минимального пути
    min_len = 1000_000_000_000
    # минимальный путь (тип переменной - кортеж)
    min_path:tuple
    # получить размерность каждой цепочки перестановок (точка-точка-точка...)
    tuple_len = len(all_paths[0])

    # исследовать все маршруты (метод перебора)
    for curr_path in all_paths:
        len_path = 0

        # сканирование текущего маршрута
        for point_num in range(tuple_len-1):
            # строка
            row = curr_path[point_num]
            # колонка
            col = curr_path[point_num+1]
            # увеличить длину маршрута
            len_path += matrix[row][col]

        if view_path:
            print(f'Путь: {curr_path}. Его длина: {len_path}')

        # если найдена очередная наименьшая длина пути
        if len_path < min_len:
            # обноваить значение
            min_len = len_path
            # запомнить саму последовательнось пути
            min_path = curr_path

    # вернуть полученное значение наименьшего пути
    return {'minlen':min_len, 'minpath':min_path}


def run(total_point=3, min_len=10, max_len=55, show_matrix=True, show_Path=False):
    delta = 2
    # получить матрицу расстояний
    points1 = get_matrix(total_point, min_len, max_len, show_matrix)
    points2 = get_matrix(total_point + delta, min_len, max_len, show_matrix)
    points3 = get_matrix(total_point + delta*2, min_len, max_len, show_matrix)
    points4 = get_matrix(total_point + delta*3, min_len, max_len, show_matrix)

    # расчитать время работы для всех матриц
    t1, len_path1 = pstopwatch(get_shortest_path, points1, show_Path, title=f'\nПодсчёт путей для {total_point} точек маршрута...')
    t2, len_path2 = pstopwatch(get_shortest_path, points2, show_Path, title=f'\nПодсчёт путей для {total_point+delta} точек маршрута...')
    t3, len_path3 = pstopwatch(get_shortest_path, points3, show_Path, title=f'\nПодсчёт путей для {total_point+delta*2} точек маршрута...')
    t4, len_path4 = pstopwatch(get_shortest_path, points4, show_Path, title=f'\nПодсчёт путей для {total_point+delta*3} точек маршрута...')

    # вывод результатов
    print(f'\nВремя проверки всех маршрутов перебором для {total_point} точек: {t1} сек.')
    print(f'Минимальный путь: {len_path1["minpath"]}. Его длина: {len_path1["minlen"]}')

    print(f'\nВремя проверки всех маршрутов перебором для {total_point+delta} точек: {t2} сек.')
    print(f'Минимальный путь: {len_path2["minpath"]}. Его длина: {len_path2["minlen"]}')

    print(f'\nВремя проверки всех маршрутов перебором для {total_point+delta*2} точек: {t3} сек.')
    print(f'Минимальный путь: {len_path3["minpath"]}. Его длина: {len_path3["minlen"]}')

    print(f'\nВремя проверки всех маршрутов перебором для {total_point+delta*3} точек: {t4} сек.')
    print(f'Минимальный путь: {len_path4["minpath"]}. Его длина: {len_path4["minlen"]}')


if __name__ == '__main__':
    run(5, 12, 35)

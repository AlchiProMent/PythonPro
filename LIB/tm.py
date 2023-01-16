# библиотечный модуль для работы с таймером
from time import *

def stopwatch(func_name, *datas, title=''):
    # подсчет времени работы функции func_names
    print('Функция {} начала работу...{}'.format(func_name.__name__, title))
    d_begin = time()
    res = func_name(*datas)
    d_end = time()
    print('Функция закончила работу.')
    return (d_end - d_begin), res

def pstopwatch(func_name, *datas, title=''):
    # особо точный подсчет времени работы функции func_names
    print('Функция {} начала работу...{}'.format(func_name.__name__, title))
    d_begin = perf_counter()
    res = func_name(*datas)
    d_end = perf_counter()
    print('Функция закончила работу.')
    return (d_end - d_begin), res




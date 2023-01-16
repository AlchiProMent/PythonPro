# профилирование
import cProfile
import requests

def lenta():
    requests.get('https://lenta.ru')

def vk():
    requests.get('https://vk.com')

def google():
    requests.get('https://google.com')

def ya():
    requests.get('https://ya.ru')

def pyorg():
    requests.get('https://python.org')

def all_loads():
    # загрузить все страницы
    lenta()
    vk()
    google()
    ya()
    pyorg()

# профилирование
cProfile.run('all_loads()', sort=2)



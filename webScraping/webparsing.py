# парсинг страницы из сети
#
from bs4 import BeautifulSoup
from urllib.request import urlopen

ID_PATTERN = '[ID]'
ACTOR_BIO_URL_PATTERN = f'https://www.kino-teatr.ru/kino/acter/m/sov/{ID_PATTERN}/bio/'
ACTOR_FILMS_URL_PATTERN = f'https://www.kino-teatr.ru/kino/acter/m/sov/{ID_PATTERN}/works/'

def get_actor_films(actor_id):
    # получить фильмы актера и вернуть в виде списка
    films_lst = []

    # получить URL страницы с описанием списка фильмов
    films_url = ACTOR_FILMS_URL_PATTERN.replace(ID_PATTERN, actor_id)
    # прочитать страницу со списком фильмов актера
    html = str(urlopen(films_url).read(), 'windows-1251')
    # сформировать DOM на основе полученного документа
    dom = BeautifulSoup(html, 'html.parser')
    # получить все блоки с описаниями фильмов
    films = dom.findAll('div', class_='film_block')
    for film in films:
        # название фильма
        name = film.find('div', class_='film_name')
        # год выхода фильма
        year = film.find('div', class_='film_year_text')
        # получить ссылку на страницу с описанием фильма
        link = film.find('a')

        if link:
            # если у блока с описанием фильма есть ссылка
            films_lst.append({'year':year.text, 'title':name.text, 'url': link.get("href")})
        else:
            films_lst.append({'year':year.text, 'title':name.text, 'url': ''})
    # вернуть отсортированный по ключу "ГОД" список фильмов
    return sorted(films_lst, key=lambda movie: movie['year'])

def view_actor_data(actor_id):
    # информация об актере

    print('\nИдет загрузка данных...\n')

    # получить URL с биографией актера
    bio_url = ACTOR_BIO_URL_PATTERN.replace(ID_PATTERN, actor_id)
    # прочитать страницу с биографией актера
    html = str( urlopen(bio_url).read(), 'windows-1251' )
    # сформировать DOM на основе полученного документа
    dom = BeautifulSoup(html, 'html.parser')

    actor = dom.find(id='page_name')
    actor_name = actor.h1.string

    # получить все фильмы актера
    all_films = get_actor_films(actor_id)

    # вывести на экран имя актера
    print(f'\n{actor_name} снималя в фильмах и спектаклях:')
    print('-'*50)
    # вывести все фильмы (начиная с самых последних)
    for film in reversed(all_films):
        if film['url'] != '':
            print(f'{film["year"]}: "{film["title"]}"')
        else:
            # если в описании фильма нет ссылки на полную страницу с описанием
            print(f'-{film["year"]}: "{film["title"]}"')

def start_parsing():
    # запуск программы парсинга
    while (actor_id := input('\nВведите ID актера (ENTER для выхода): ')) != '':
        if actor_id != '':
            # если пользователь ввел ID актера - вывести информацию об актере и его фильмах
            view_actor_data(actor_id)

if __name__ == '__main__':
    start_parsing()

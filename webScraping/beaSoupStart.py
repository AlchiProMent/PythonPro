# знакомство с BeautifulSoup4
import bs4

try:
    # открыть HTML-файл
    with open('HTML/index.html', encoding='UTF-8') as f:
        # прочитать текст из файла
        html = f.read()
except:
    print('Ошибка чтения файла!')
else:
    # выполнить парсинг
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # создать пустой словарь
    tags_dict = {}
    # просмотреть всё дерево дочерних элементов
    for child in soup.recursiveChildGenerator():

        # если это тег
        if child.name:
            if child.attrs:
                print(child.name, child.attrs)

            # увеличить счетчик на единицу или добавить элемент в справочник
            if child.name in tags_dict.keys():
                tags_dict[child.name] += 1
            else:
                # этого тега ещё нет в спрвочнике
                tags_dict.update({child.name: 1})

    # вывести справочник на экран
    print()
    for key, val in tags_dict.items():
        print(f'{key}: {val}')

    print()
    # заголовок документа
    print(soup.title)
    print(soup.title.string)

    print()
    # учетная информация
    metas = soup.findAll('meta')
    print(*metas, sep='\n')
    print(f'{metas[0]["charset"]}')
    print(f'{metas[1]["name"]}: {metas[1]["content"]}')
    print(f'{metas[2]["name"]}: {metas[2]["content"]}')

    print()
    links = soup.findAll('link')
    print(*links, sep='\n')
    print(f'Подключается файл: {links[0]["href"]}')

    print()
    # заголовки
    print(soup.h1.string)
    h2 = soup.findAll('h2')
    print(h2[0].string)
    print(h2[1].string)

    print()
    for anchor in soup('a'):
        url = anchor.get('href')
        print(url)

    print()
    # элементы списка
    li = soup.findAll('li')
    for s in li:
        if s.strong:
            print(s.string)
        else:
            print('\t', s.string)

    print()
    # выбрать все теги класса image
    divs = soup.findAll('div', class_='image')

    for div in divs:
        print(f'{div.img.name}: {div.img.attrs["src"]}')
        print(div.img.attrs)
        if div.p:
            print(div.p.string)


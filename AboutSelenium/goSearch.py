# пример работы с поисковым сервисом Google
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# адрес сайта
GOOGLE_URL = 'https://www.google.com'


def print_links(urls, index):
    # вывести ссылки на консоль
    print(f'[ {index} ]')
    for link in urls:
        # получить URL через атрибут HREF
        url = link.get_attribute('href')
        # вывести адрес на консоль
        print(url)

def go_search(query_text, make_scr=False):
    # создать объект для настройки опций
    opts = Options()
    # установить стратегию загрузки
    opts.page_load_strategy = 'normal'
    # создать драйвер с учетом новой опции
    driver = webdriver.Chrome(options=opts)
    # загрузить страницу
    driver.get(GOOGLE_URL)

    # получить строку ввода поискового запроса
    text_box = driver.find_element(by=By.NAME, value='q')
    # поместить запрос в строку ввода
    text_box.send_keys(query_text)
    # нажать на ENTER (RETURN)
    text_box.send_keys(Keys.RETURN)

    # цикл загрузки десяти страниц
    for i in range(1, 11):
        # задержка в 3 секунды
        driver.implicitly_wait(3)
        # сделать скриншот страницы
        if make_scr:
            driver.save_screenshot(f'scr/screen_{i:02}.png')
        # все ссылки, который Google выдал по запросу
        links = driver.find_elements(by=By.XPATH, value='//*[@class="yuRUbf"]/a')
        # вывести все ссылки страницы
        print_links(links, i)

        # получить ссылку на следующую страницу
        next_link = driver.find_element(by=By.ID, value='pnnext').get_attribute('href')
        # загрузить эту страницу
        driver.get(next_link)

    # закрыть драйвер и выйти
    driver.close()
    driver.quit()

if __name__ == '__main__':
    query_text = 'Программирование'
    go_search(query_text, True)
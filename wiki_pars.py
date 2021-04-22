import requests
import re
import sys

from bs4 import BeautifulSoup as bs
from pandas import Series

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
base_url = 'https://ru.wikipedia.org/'

animal = set()


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def get_data(html):
    soup = bs(html, 'lxml')
    animals = soup.find('div', class_='mw-category-group').find_all('li')

    for anim in animals:
        if (anim.find('a').string)[0].lower() == 'a':
            s = Series(word[0] for word in animal)
            print(s.value_counts())
            sys.exit(0)
        animal.add(anim.find('a').string)


def main():
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

    while True:
        get_data(get_html(url))

        soup = bs(get_html(url), 'lxml')

        try:
            pattern = 'Следующая страница'
            url = base_url + soup.find(
                                       'div', id='mw-pages').find(
                                       'a', text=re.compile(pattern)).get(
                                       'href')
        except:
            break


if __name__ == '__main__':
    main()

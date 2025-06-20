import requests
from bs4 import BeautifulSoup as bs

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
animals = {}

while not url == '':
    result = requests.get(url)
    if not result.status_code == 200:
        print(f'Error: {result.status_code}')
        break
    soup = bs(result.text, 'html.parser')
    a = soup.find('a', string='Следующая страница')
    if a:
        url = 'https://ru.wikipedia.org' + a['href']
    else:
        url = ''
    for l in soup.select('.mw-category-columns li > a'):
        s = l.text[0]
        if s in animals:
            animals[s] += 1
        else:
            animals[s] = 1

with open('beasts.csv', 'w', encoding='UTF-8') as f:
    for e in sorted(animals):
        f.write(f'{e},{animals[e]}\n')

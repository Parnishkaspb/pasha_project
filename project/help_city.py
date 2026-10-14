import requests
from bs4 import BeautifulSoup

url = 'https://hramy.ru/regions/city_abc.htm'

# Отправляем GET-запрос на страницу и получаем HTML-код
response = requests.get(url)
html = response.text

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html, 'html.parser')

# Находим таблицу с классом "prezaprox"
table = soup.find('table', class_='prezaprox')

# Находим все строки таблицы
rows = table.find_all('tr')[1:]

# Извлекаем названия городов из каждой строки таблицы
cities = []
for row in rows:
    # Извлекаем ячейку с названием города (предполагая, что она находится в первой ячейке каждой строки)
    cell = row.find('td')
    if cell:
        city = cell.text.strip()
        # city = city.encode('utf-8')
        # try:
        #     city = city.encode('cp1251')
        # except:
        #     pass
        cities.append(city)

# Выводим список городов
for city in cities:
    print(city)

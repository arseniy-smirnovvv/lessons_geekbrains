# Метод получения курса валюта через распарсинг строки модулуем Вкусный суп
import requests
from bs4 import BeautifulSoup as BS

def currency_rates(char_code):
    char_code = char_code.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    for valute in soup.findAll('valute'):
        if char_code == valute.find('charcode').text:
            return float(valute.find('value').text.replace(',', '.'))
    return None

print(currency_rates('USD'))
print(currency_rates('usd'))
print(currency_rates('EUR'))
# Метод получения курса валюта через распарсинг строки модулуем elementtree
import xml.etree.ElementTree as ET
import requests


def currency_rates(char_code):
    char_code = char_code.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)

    for valute in ET.fromstring(response.text).findall('Valute'):
        if char_code == valute.find('CharCode').text:
            return float(valute.find('Value').text.replace(',', '.'))

    return None


print(currency_rates('USD'))
print(currency_rates('usd'))
print(currency_rates('EUR'))

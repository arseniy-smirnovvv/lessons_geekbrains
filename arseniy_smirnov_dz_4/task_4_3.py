# Я выбрал метод решения второй задачи с помощью Element Tree, посколько он показался мне самым простым.
import xml.etree.ElementTree as ET
from datetime import datetime as DT
import requests


def convert_header_date(header_date, format):
    date = DT.strptime(header_date, '%a, %d %b %Y %H:%M:%S %Z')
    return DT.strftime(date, format)


def currency_rates(char_code):
    char_code = char_code.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    date = convert_header_date(response.headers['Date'], '%Y-%m-%d')

    for valute in ET.fromstring(response.text).findall('Valute'):
        if char_code == valute.find('CharCode').text:
            return f"{float(valute.find('Value').text.replace(',', '.'))}, {date}"

    return None


print(currency_rates('USD'))
print(currency_rates('usd'))
print(currency_rates('EUR'))

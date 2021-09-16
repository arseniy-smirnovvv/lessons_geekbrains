# Метод получения курса валюта через str (без использования каких-либо библиотек за исключением request)
import requests


def currency_rates(char_code):
    # Поскольку все char коды в верхнем регистре, то принимаемый можно перевести в верхний
    char_code = char_code.upper()

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    valute_lst = []
    response = requests.get(url).text
    # Получаем XML код, где находятся все валюты
    response = response[response.find('<ValCurs'):response.find('</ValCurs>')]

    # Добавляем xml код каждой валюты в список
    while response.find('<Valute') != -1:
        start = response.find('<Valute')
        end = response.find('</Valute>') + len('</Valute>')
        valute_lst.append(response[start:end])
        response = response[end:]

    # Теперь просто перебираем список с валютами и ищем в них наш char_code, ну а потом возврвщаем курс
    for valute in valute_lst:
        if valute.find(char_code) != -1:
            start = valute.find('<Value>') + len('<Value>')
            end = valute.find('</Value>')
            return float(valute[start:end].replace(',', '.'))

    # Если ничего не нашел, то возвращает None
    return None


print(currency_rates('RUB'))
print(currency_rates('USD'))
print(currency_rates('usD'))
print(currency_rates('EUR'))
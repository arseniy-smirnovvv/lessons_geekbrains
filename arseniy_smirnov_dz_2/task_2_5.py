prices = [81.73, 34, 76.42, 20.22, 80.7, 66.13, 98.27, 61, 22.86, 7.03, 1.1, 8, 36.76, 62.89, 81.26, 72.94, 85.59, 92.63, 24.96, 52.5, 59]
discend_price = []
price_id = id(prices)
result = ''

# A
print('ПУНКТ А')
for idx, price in enumerate(prices):
    lst_price = str(price).split('.')
    rubles = f'{lst_price[0]:0>2}'
    if len(lst_price) > 1:
        penny = f'{lst_price[1]:0<2}'
    else:
        penny = '00'

    result += f"{rubles} руб {penny} коп; "
    prices[idx] = f"{rubles}.{penny}"
print(result)

# B
print("ПУНКТ B")
prices.sort()
print('Список отсортирован:')
print(prices)
print(f'id в памяти старого списка - {price_id} = {id(prices)} - id в памяти нового отсортированного спика ')

# C
print('ПУНКТ С')
prices.sort(reverse=True)
for price in prices:
    discend_price.append(price)
print('Список отсортирован по убыванию: ')
print(discend_price)

# D
# Поскольку у нас есть список с отсортированными ценами по убыванию, то лучше всего будет использовать срезы)
print(sorted(discend_price[:5], reverse=True))
# Мы могли бы использовать просто вывод списка со срезами, но все же тут главное понять функция sorting или sort)
# print(discen_price[:5])


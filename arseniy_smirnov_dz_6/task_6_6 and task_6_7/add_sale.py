import sys

if (len(sys.argv) <= 1):
    sys.exit('Введите сумму которую хотите добавить! python add_sale.py <сумма>')

file_name = 'bakery.csv'
summ = sys.argv[1]

with open(file_name, 'a', encoding='utf-8') as f:
    if not f.write(summ + '\n'):
        print('Произошла ошибка!')
    else:
        print(f'{summ} успешно записалось в файл {file_name}')

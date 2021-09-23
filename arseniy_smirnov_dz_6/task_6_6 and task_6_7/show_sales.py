import sys

file_name = 'bakery.csv'
tmp_lst = []
with open(file_name, 'r', encoding='utf-8') as f:
    line = f.readline().replace('\n', '')
    while line:
        tmp_lst.append(line)
        line = f.readline().replace('\n', '')

len_tmp_lst = len(tmp_lst)

if len_tmp_lst == 0:
    sys.exit('Таблица пустая.')

if len(sys.argv) == 1:
    [print(el) for el in tmp_lst]
elif len(sys.argv) == 2:
    start = int(sys.argv[1]) - 1
    if start > len_tmp_lst:
        sys.exit(f'Значение которое вы ввели превышает длинну таблицы! Всего значений в таблице: {len_tmp_lst}')
    # У меня есть сомнения по поводу, хорошая ли практика использовать генарторы для вывода значений. Пожалуйста дай обртную связь по этому поводу
    [print(el) for el in tmp_lst[start:]]
elif len(sys.argv) == 3:
    start = int(sys.argv[1]) - 1
    stop = int(sys.argv[2])
    if start > len_tmp_lst:
        sys.exit(f'Значение которое вы ввели превышает длинну таблицы! Всего значений в таблице: {len_tmp_lst}')
    if start > stop or start == stop:
        sys.exit(f'Стартовое положение не может быть меньше положения на котором нужно останавливаться!')
    [print(el) for el in tmp_lst[start:stop]]
else:
    sys.exit('Введите python show_sales.py <start> <stop> - последние 2 флага не обязательные.')
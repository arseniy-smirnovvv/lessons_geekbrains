import sys


def get_all(file_name):
    tmp_lst = []
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            tmp_lst.append(line)
            line = f.readline()
    return tmp_lst


def edit_sale(rec_num, new_summ, file_name):
    summ_lst = get_all(file_name)
    rec_num -= 1
    if rec_num + 1 > len(summ_lst):
        return f'Элемента под номером {rec_num + 1} не существует!'
    last_summ = summ_lst[rec_num].replace('\n', '')
    summ_lst[rec_num] = new_summ + '\n'
    with open(file_name, 'w', encoding='utf=8') as f:
        f.writelines(summ_lst)
    return f'Элемент под номер {rec_num + 1} изменился с {last_summ} на {new_summ}'


file_name = 'bakery.csv'

if len(sys.argv) < 3 or len(sys.argv) > 3:
    [print('[{}] => {}'.format(idx + 1, el.replace("\n", ""))) for idx, el in enumerate(get_all(file_name))]
    sys.exit('Введите python edit_sale.py <rec_num> <new_summ>')

sys.exit(edit_sale(int(sys.argv[1]), sys.argv[2], file_name))

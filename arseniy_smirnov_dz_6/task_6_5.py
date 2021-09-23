import json
import os
import sys
import time


def write_serializate_date(result_file, dict):
    with open(result_file, 'w', encoding='utf-8') as f:
        if json.dump(dict, f) == None:
            return True


def check_file(file_name):
    if not os.path.exists(file_name):
        return False
    else:
        return True




def get_date_file(file_name):
    tmp_lst = []
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readline().replace('\n', '')
        while line:
            tmp_lst.append(line)
            line = f.readline().replace('\n', '')
    return tmp_lst


def parse_table(names_table, hobbie_table):
    tmp_dict = {f"{key}": {} for key in range(len(names_table))}
    for key, person in zip(tmp_dict.keys(), names_table):
        person = person.split(',')
        tmp_dict[f"{key}"]['firstname'] = person[0]
        tmp_dict[f"{key}"]['lastname'] = person[1]
        tmp_dict[f"{key}"]['surname'] = person[2]
        if int(key) < len(hobbie_table):
            tmp_dict[f"{key}"]['hobbie'] = hobbie_table[int(key)]
        else:
            tmp_dict[key]['hobbie'] = None
    return tmp_dict


if len(sys.argv) < 4:
    sys.exit('Введите <script_name> <table_1.csv> <table_2.csv> <result_file.json>')

if not check_file(sys.argv[1]) or not check_file(sys.argv[2]):
    print('Файл не найден! Проверьте корректность данных!')
    sys.exit()

name_table = sys.argv[1]
hobbie_table = sys.argv[2]
result_file = sys.argv[3]

result_dict = parse_table(get_date_file(name_table), get_date_file(hobbie_table))
if write_serializate_date(result_file, result_dict):
    print(f'Данные обработались и успешно сохранились в файле {result_file} в формате JSON. При load будет возвращаться словарь.')

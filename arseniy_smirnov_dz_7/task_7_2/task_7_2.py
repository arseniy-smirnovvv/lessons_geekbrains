# Я долго решил задачу с решением над парсингом данных без использования библиотеки
# Решение заняло около 3 днех, в итоге что-то получилось
# Честно, я до сих пор не понимаю как она работает, но она работае и это главное.
import json
import os


def create_starter(starter_dict, path=os.getcwd()):
    if not isinstance(starter_dict, dict): raise Exception('Неверный формат данных стартера!')
    for name, values in starter_dict.items():
        dir_path = os.path.join(path, name)
        if isinstance(values, dict):
            if not os.path.exists(dir_path):
                if len(name.split('.')) > 1:
                    open(dir_path, 'a').close()
                else:
                   os.mkdir(dir_path)
            create_starter(values, dir_path)
        elif not (values is None):
            raise Exception('Неверный формат подкаталога стартера!')
        if not os.path.exists(dir_path):
            if len(name.split('.')) > 1:
                open(dir_path, 'a').close()
            else:
                os.mkdir(dir_path)
    return True


def find_stop_index(data, level):
    stop = 0
    for idx, word in enumerate(data):
        if idx + 1 >= len(data):
            stop += 1
            break
        level_bash = word.count('-')
        if level == level_bash:
            return idx
        stop = idx + 1
    return stop


def parse_yaml(data):
    data.append('')
    r_dict = {}
    idx = 0
    while idx <= len(data):
        if idx + 1 >= len(data):
            break
        word = data[idx]
        if word == '':
            idx += 1
            continue
        key = word.replace('-', '')
        next_word = data[idx + 1]
        level_bash = word.count('-')
        next_level_bash = next_word.count('-')
        if next_level_bash > level_bash:
            start = idx + 1
            stop = find_stop_index(data[start:], level_bash)
            r_dict[key] = parse_yaml(data[start:stop + start])
            idx += stop
        else:
            r_dict[key] = None
        idx += 1
    return r_dict


with open('config.yaml', 'r') as f:
    yaml_data = [line.replace(' ', '-').replace('\n', '') for line in f.readlines()]
    yaml_data.append('')
starter_dict = parse_yaml(yaml_data)
create_starter(starter_dict)

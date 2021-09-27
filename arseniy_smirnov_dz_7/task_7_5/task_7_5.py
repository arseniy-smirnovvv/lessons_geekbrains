import json
import os


def write_json_table(table, folder_name):
    file_name = f'{folder_name}_summary.json'
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(table, f)
    except Exception as e:
        raise e


def size_table(folder):
    if not os.path.exists(folder): raise FileNotFoundError('Такой директории не сущесвтует!')
    files_size = []
    files_type = []
    for address, dirs, files in os.walk(folder):
        [(
            (files_size.append(os.path.getsize(os.path.join(address, file)))),
            files_type.append(os.path.splitext(file)[1]))
            for file in files]
    files = [(size, type_f) for size, type_f in zip(files_size, files_type)]
    # Сначала мы формируем таблица. Это позволит нам охватить все файла, которые будут передаваться в функцию.
    table_dict = {}
    max_size = max(files_size)
    count_null = 0
    while max_size:
        max_size = max_size // 10
        count_null += 1
    max_step = int(f'1{"0" * (count_null - 1)}')
    while max_step:
        table_dict[max_step] = (0, [])
        max_step = max_step // 10
        if max_step == 1:
            table_dict[0] = (0, [])
            break
    # Потом уже распредялем размеры файлов по этой таблице
    for size, type_f in files:
        for step in table_dict:
            if size >= step:
                tuple_dict = list(table_dict[step])
                tuple_dict[0] += 1
                tuple_dict[1].append(type_f)
                table_dict[step] = tuple(tuple_dict)
    return table_dict


folder = 'some_data'
try:
    table = size_table(folder)
    # Функция чисто для красивого вывода
    print(json.dumps(table, indent=2))
    write_json_table(table, folder)
except Exception as e:
    print(e)

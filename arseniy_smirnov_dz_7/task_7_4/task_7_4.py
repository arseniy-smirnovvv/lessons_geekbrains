import os


def size_table(folder):
    if not os.path.exists(folder): raise FileNotFoundError('Такой директории не сущесвтует!')
    files_size = []
    for address, dirs, files in os.walk(folder):
        for file in files:
            files_size.append(os.path.getsize(os.path.join(address, file)))
    # Сначала мы формируем таблицу. Это позволит нам охватить все файла, которые будут передаваться в функцию.
    table_dict = {}
    max_size = max(files_size)
    count_null = 0
    while max_size:
        max_size = max_size // 10
        count_null += 1
    max_step = int(f'1{"0" * (count_null - 1)}')
    while max_step:
        table_dict[max_step] = 0
        max_step = max_step // 10
        if max_step == 1:
            table_dict[0] = 0
            break
    # Потом уже распредялем размеры файлов по этой таблице
    for size in files_size:
        for step in table_dict:
            if size >= step:
                table_dict[step] += 1
    return table_dict


'''
Проверка, в папке test у нас один файл размером 1 мб, два файла размером 100 байт и один файл 7 байт'''
folder = 'test'
try:
    print(size_table(folder))
except Exception as e:
    print(e)
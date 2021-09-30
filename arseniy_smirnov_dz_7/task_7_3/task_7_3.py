import os
# Я подключил shutill, что бы посмотреть как он работает. Я мог бы и не использовать его.
import shutil


def move_files(folder_name, move_dir, file_type):
    for addres, dirs, files in os.walk(folder_name):
        if not len(files) == 0:
            for file in files:
                if os.path.splitext(file)[-1] == file_type:
                    addres_lst = addres.split('\\')
                    if addres_lst[1] == 'template': continue
                    # Добавляем в путь до файла папку, в которой будет хранить эти все файлы
                    addres_lst.insert(addres_lst.index(folder_name) + 1, move_dir)
                    # Собираем этот путь
                    dir_path = os.path.join(*addres_lst)
                    # Получаем текущий путь до файла
                    file_path = os.path.join(addres, file)
                    # Создаём такой же путь в папке templates
                    # Я хотел использовать makedirs, но она как-то некоректно работае
                    dir_create = ''
                    for dir in addres_lst:
                        dir_create = os.path.join(dir_create, dir)
                        if not os.path.isdir(dir_create):
                            os.mkdir(dir_create)
                    try:
                        shutil.copy2(file_path, os.path.join(dir_path, file))
                    except shutil.SameFileError:
                        continue


folder_name = 'my_project'

try:
    move_files(folder_name, 'templates', '.html')
except FileNotFoundError as e:
    print(e)
    print('Заданной директории не существует!')

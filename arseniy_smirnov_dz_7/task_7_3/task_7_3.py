import os
# Я подключил shutill, что бы посмотреть как он работает. Я мог бы и не использовать его.
import shutil


def move_files(folder_name, move_dir, file_type):
    move_path = os.path.join(folder_name, move_dir)
    if not os.path.exists(move_path):
        os.mkdir(move_path)

    for addres, dirs, files in os.walk(folder_name):
        if not len(files) == 0:
            for file in files:
                if os.path.splitext(file)[-1] == file_type:
                    dir_name = os.path.split(addres)[-1]
                    dir_path = os.path.join(folder_name, move_dir, dir_name)
                    file_path = os.path.join(addres, file)
                    if not os.path.isdir(dir_path):
                        os.mkdir(dir_path)
                    try:
                        shutil.copy2(file_path, os.path.join(dir_path, file))
                    except shutil.SameFileError:
                        pass


folder_name = 'my_project'

try:
    move_files(folder_name, 'templates', '.html')
except FileNotFoundError as e:
    print('Заданной директории не существует!')

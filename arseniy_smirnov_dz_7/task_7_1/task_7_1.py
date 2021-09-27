import os


def create_starter(starter_dict, path=os.getcwd()):
    if not isinstance(starter_dict, dict): raise Exception('Неверный формат данных стартера!')
    for name, values in starter_dict.items():
        dir_path = os.path.join(path, name)
        if isinstance(values, dict):
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            create_starter(values, dir_path)
        elif not (values is None):
            raise Exception('Неверный формат подкаталога стартера!')
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    return True


try:
    starter_dict = {
        'my_project': {
            'settings': None,
            'mainapp': None,
            'adminapp': None,
            'authapp': None,
            'testingapp': {
                'it`s ok': None
            }
        }
    }
    create_starter(starter_dict)
except Exception as e:
    print(e)

# Проверяем на вхождение неправильного стартера
try:
    a = 5
    create_starter(a)
except Exception as e:
    print(e)

# Проверяем на вхождение правильного стартера, с неправильным под каталогом
try:
    starter_dict2 = {
        'my_project': [
            'settings',
            'mainapp'
        ]
    }
    create_starter(starter_dict2)
except Exception as e:
    print(e)

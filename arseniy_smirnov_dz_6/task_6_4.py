import sys
import json


names = []
hobbie = []

with open('files/users.csv', 'r', encoding='utf-8') as f:
    line = f.readline().replace('\n', '')
    while line:
        names.append(line)
        line = f.readline().replace('\n', '')

with open('files/hobby.csv', 'r', encoding='utf-8') as f:
    line = f.readline().replace('\n', '')
    while line:
        hobbie.append(line)
        line = f.readline().replace('\n', '')

# Создаём ключи со с пустыми словарями внутри
person_dict = {key: {} for key in range(len(names))}


# Мы получаем список с фио и хобби, и помещаем его в словарь
# Почему в словарь? на мой взгляд, самый лучший способ структрурировать данные
for key, person in zip(person_dict.keys(), names):
    person = person.split(',')
    person_dict[key]['firstname'] = person[0]
    person_dict[key]['lastname'] = person[1]
    person_dict[key]['surname'] = person[2]
    if key < len(hobbie):
        person_dict[key]['hobbie'] = hobbie[key]
    else:
        person_dict[key]['hobbie'] = None


# я не понял, нужно ли сериализовать данные, но на всякий случай сделаем. Все таки тема про это )
with open('files/date_task_2.json', 'w', encoding='utf-8') as f:
    json.dump(person_dict, f)

with open('files/date_task_2.json', 'r', encoding='utf-8') as f:
    result_dict = json.load(f)

# Получаем на выходе словарь с ключем id юзера, и значениямим словаями его данных
space = ' ' * 4
for key, person in result_dict.items():
    print(f"{key} =>")
    print(f"{space}Имя - {person['firstname']}")
    print(f"{space}Фамилия- {person['lastname']}")
    print(f"{space}Отчество - {person['surname']}")
    print(f"{space}Хобби - {person['hobbie']}")
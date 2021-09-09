# Поиск имен сотрудников среди искаженных данных без создания нового списка
names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Делаем корретные имена
for idx, word in enumerate(names):
    phrase = word.split(' ')[:-1]
    name = word.split(' ')[-1].capitalize()
    names[idx] = f"{' '.join(phrase)} {name}"
    print(f'Привет, {name}!')

print(names)



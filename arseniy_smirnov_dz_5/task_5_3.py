tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Денис', 'Арсений', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

result = ((tutors[i], (klasses[i] if len(klasses) > i else None)) for i in range(len(tutors)))
# Доказываем, что это генератор
print(type(result))
# Выводим этот генератор
print(* result)
# После вывода генаратора, мы его истощили
print(* result)


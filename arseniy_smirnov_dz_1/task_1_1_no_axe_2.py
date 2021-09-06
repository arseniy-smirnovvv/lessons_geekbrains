# Пользователь вводит количество секунд и сразу преобразовываем в секунды
duration = int(input('Введите количество секунд: '))
# Создаём кортеж, зная какие будут последовательности
step = ('дн', 60 * 60 * 24, 'час', 60 * 60, 'мин', 60)
result = ''
# Отличие от первого способа, тем, что он проверяет кортеж наоборот, тут стоит условие
# если введенное количество секунд меньше коичество секунд в элементе кортежа, то и последующие элементы
# будут меньше, и смысла продолжать цикл нет
for idx in range(len(step) - 1, 0, -2):
    val_step = step[idx]
    name_step = step[idx - 1]
    if duration < val_step:
        break
    result = f'{duration // val_step} {name_step} ' + result
    duration -= (duration // val_step) * val_step

if duration != 0:
    result += f'{duration} сек'

print(result)
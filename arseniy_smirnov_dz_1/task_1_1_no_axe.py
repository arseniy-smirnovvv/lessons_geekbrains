# Пользователь вводит количество секунд и сразу преобразовываем в секунды
duration = int(input('Введите количество секунд: '))
# Создаём кортеж, зная какие будут последовательности
step = ('дн', 60 * 60 * 24, 'час', 60 * 60, 'мин', 60)
result = ''

for idx in range(1, len(step), 2):
    val_step = step[idx]
    name_step = step[idx - 1]
    if duration > val_step:
        result += f'{duration // val_step} {name_step} '
        duration -= (duration // val_step) * val_step

if duration != 0:
    result += f'{duration} сек'

print(result)
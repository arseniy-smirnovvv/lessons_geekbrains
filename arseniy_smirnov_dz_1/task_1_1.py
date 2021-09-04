# Пользователь вводит количество секунд и сразу преобразовываем в секунды
duration = int(input('Введите количество секунд: '))
# Переменные, которые содержат количество секунд в дне, часе, минуте
one_minute = 60
one_hour = 60 * one_minute
one_day = 24 * one_hour
# Переменная для вывода конечного результата
result = ''

if duration > one_day:
    count_day = duration // one_day
    duration -= count_day * one_day
    result += f'{count_day} дн '
if duration > one_hour:
    count_hour = duration // one_hour
    duration -= count_hour * one_hour
    result += f'{count_hour} час '
if duration > one_minute:
    count_hour = duration // one_minute
    duration -= count_hour * one_minute
    result += f'{count_hour} мин '

if duration != 0:
    result += f'{duration} сек'

print(result)
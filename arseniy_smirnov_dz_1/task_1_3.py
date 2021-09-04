# Список с числами исключеними
lst_exec = [12, 13, 14]
for num in range(1, 101):
    last_num = str(num)[-1]
    last_num = int(last_num)
    if last_num == 1 and num != 11:
        print(num, 'процент')
    elif (last_num == 2 or last_num == 3 or last_num == 4) and num not in lst_exec:
        print(num, 'процента')
    else:
        print(num, 'процентов')
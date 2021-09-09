lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numeric = ['1', '2', '3', "4", "5", "6", "7", "8", "9"]
result_lst = []

# Разбиваем список на  слова
for word in lst:
    num_idx = []
    for idx, letter in enumerate(word):
        if letter in numeric:
            num_idx.append(idx)

    if len(num_idx) > 0:
        if len(num_idx) == 1:
            num = word[num_idx[0]]
            word = list(word)
            word[num_idx[0]] = f'{num:0>2}'
            word = ''.join(word)
        result_lst.append('"')
        result_lst.append(word)
        result_lst.append('"')
    else:
        result_lst.append(word)

# А теперь выводим строку, что бы перед числами и ковычками не было пробела
idx_list = 0
while idx_list < len(result_lst):
    if result_lst[idx_list] == '"':
        print(f'"{result_lst[idx_list + 1]}" ', end='')
        idx_list += 3
    else:
        print(f'{result_lst[idx_list]} ', end='')
        idx_list += 1
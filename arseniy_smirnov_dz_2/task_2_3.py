# Решение второй задачи без создания нового списка
lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numeric = ['1', '2', '3', "4", "5", "6", "7", "8", "9"]

len_lst = len(lst)
idx = 0

while idx < len_lst:
    word = lst[idx]
    count_num = []
    add_quotes = False

    for let_idx, letter in enumerate(word):
        if letter in numeric:
            if not add_quotes:
                lst.insert(idx, '"')
                lst.insert(idx + 2, '"')
                idx += 2
                len_lst = len(lst)
                add_quotes = True
            count_num.append(let_idx)
    if len(count_num) == 1:
        edit_word = list(lst[idx - 1])
        edit_idx = count_num[0]
        edit_word[edit_idx] = f'{word[edit_idx]:0>2}'
        lst[idx - 1]= ''.join(edit_word)
    idx += 1

print(lst)

idx = 0
while idx < len(lst):
    if lst[idx] == '"':
        print(f'"{lst[idx + 1]}" ', end='')
        idx += 3
    else:
        print(f'{lst[idx]} ', end='')
        idx += 1
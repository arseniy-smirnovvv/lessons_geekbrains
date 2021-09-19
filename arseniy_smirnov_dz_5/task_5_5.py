src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def count_val(lst):
    tmp_dict = {}
    for el in lst:
        if el in tmp_dict:
            tmp_dict[el] += 1
        else:
            tmp_dict[el] = 0
    return tmp_dict


# 1 способ
dict_src = count_val(src)
result = [num for num, count in dict_src.items() if count == 0]
print(result)


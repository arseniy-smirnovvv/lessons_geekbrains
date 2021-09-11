def thesaurus(*args):
    resut_dict = {}
    for name in args:
        tmp_list = []
        first_let = name[0]
        if resut_dict.get(first_let):
            if isinstance(resut_dict[first_let], list):
                tmp_list = resut_dict[first_let]
            else:
                tmp_list.append(resut_dict[first_let])
            tmp_list.append(name)
            resut_dict[first_let] = tmp_list
        else:
            resut_dict[first_let] = name
    return resut_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", 'Илюха', 'Илья'))

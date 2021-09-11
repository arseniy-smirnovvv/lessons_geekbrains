# Сложны код для понимания, поэтому я лучше все закоментирую)
def thesaurus_adv(*args):
    # Создаём словарь, где будет хранится конечные словари
    result_dict = {}
    # Пробегаемся по каждому аргументы, в которых хранятся строки с именем и фамилиями сотрудников
    for name in args:
        # Создаём промежуточный словарь и список
        tmp_dict = {}
        tmp_list = []
        # Получаем первую букву имени, и первую букву фамилии
        fs_name_let = name.split(' ')[0][0]
        ls_name_let = name.split(' ')[1][0]
        # Если в словаре уже есть ключ с первой буквой фамилии
        if result_dict.get(ls_name_let):
            # Если в словаре есть уже ключ с первой буквой фамилии и с первой буквой имени
            if result_dict.get(ls_name_let).get(fs_name_let):
                tmp_val = result_dict.get(ls_name_let).get(fs_name_let)
                # Если значения словаря это список, тогда мы присваеваем временной переменной этот список
                if isinstance(tmp_val, list):
                    tmp_list = tmp_val
                else:
                    # Если к примеру это не список, а лишь самое первое значение которое мы добавили, то мы добавляем
                    # его в список
                    tmp_list.append(tmp_val)
                # А  потом мы добавляем ФИ сотрудника
                tmp_list.append(name)
                # И этот список уже добавляем в словарь с ключем первой буквы фамилии в котором славрь с ключем
                # первый буквы имени этого ФИ
                result_dict[ls_name_let][fs_name_let] = tmp_list
            # Если нет, то мы создаём в этом словаре, словарь с первой буквой имени и самого ФИ сотрудника
            else:
                tmp_dict[fs_name_let] = name
                result_dict[ls_name_let].update(tmp_dict)
        # Если нету, то мы создаём ключ и присваиваем в него словарь с ключом первой буквы имени и самого ФИ сотрудника
        else:
            tmp_dict[fs_name_let] = name
            result_dict[ls_name_let] = tmp_dict

    return result_dict


result = thesaurus_adv("Иван Сергеев",
                       "Инна Серова",
                       "Петр Алексеев",
                       'Илона Святославовна',
                       "Илья Иванов",
                       "Анна Савельева")

# Здесь просто красивый вывод
for ls_dict in result.items():
    print(ls_dict[0], '=> ')
    for let, val in ls_dict[1].items():
        print(f'   {let} => {val}')








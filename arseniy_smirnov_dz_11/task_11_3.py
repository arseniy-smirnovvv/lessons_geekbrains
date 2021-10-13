class NoNumeric(Exception):
    def __init__(self, txt):
        self.txt = txt


tmp_lst = []

while True:
    try:
        tmp = input('Введите число, что бы добавить его в список: ')
        if tmp == 'stop':
            raise StopIteration
        elif (isinstance(tmp, str) and not tmp.isnumeric()) or isinstance(tmp, (float, int)):
            raise NoNumeric('Веденные вами данные не являются числом!')
        tmp_lst.append(tmp)
        print(f'Вы добавили число {tmp}')
    except NoNumeric as e:
        print(e)
    except StopIteration as e:
        print('Вы составили список из чисел:\n', *tmp_lst)
        break

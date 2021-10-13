import re


class Data:

    def __init__(self, str_data):
        self.dt = Data.check_data(Data.parse_data(str_data))

    @classmethod
    def parse_data(cls, data):
        template = r'(\d{2})-(\d{2})-(\d{4})'
        tmp_lst = re.findall(template, data)
        if len(tmp_lst) == 0:
            raise ValueError('Неправильный строка с датой!')
        return {
            'day': int(tmp_lst[0][0]),
            'month': int(tmp_lst[0][1]),
            'year': int(tmp_lst[0][2])
        }

    @staticmethod
    def check_data(dt_dict):
        if any([True if val <= 0 else False for val in dt_dict.values()]):
            raise ValueError('Значения не могут быть отрицательными!')
        if dt_dict['month'] > 12:
            raise ValueError('Количество месяцев не может превышать больше 12!')
        # Отбросим то, что в месяцах разное кол-во дней
        if dt_dict['day'] > 31:
            raise ValueError('В месяце не может быть больше 31 дня!')
        return dt_dict


    def __str__(self):
        return str(self.dt)


try:
    dt = Data('12-04-1231')
    print(dt)
except Exception as e:
    print(e)

try:
    dt = Data('54-04-1231')
    print(dt)
except Exception as e:
    print(e)

try:
    dt = Data('28-44-1231')
    print(dt)
except Exception as e:
    print(e)

try:
    dt = Data('54-04-sad')
    print(dt)
except Exception as e:
    print(e)

try:
    dt = Data('asd')
    print(dt)
except Exception as e:
    print(e)
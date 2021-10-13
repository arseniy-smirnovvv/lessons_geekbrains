class OfficeWarehouse:
    def __init__(self, num, name_manager):
        self.num = num
        self.name_manager = name_manager

    # PROPERTY
    @property
    def num(self):
        return self._num

    @property
    def name_manager(self):
        return self._name_manager

    # SETTERS
    @num.setter
    def num(self, val):
        if isinstance(val, str) and not val.isnumeric():
            raise ValueError('id склада должно быть числом!')
        if not isinstance(val, (int, float)):
            raise ValueError('id склада должен быть числом!')
        if val < 0:
            raise ValueError('id склада не должен быть отрицательным!')
        self._num = val

    @name_manager.setter
    def name_manager(self, name):
        if not isinstance(name, str):
            raise ValueError('имя менеджера должно быть строкой!')
        self._name_manager = name


class OfficeEquipment:

    def __init__(self, id, name, power):
        self.id = id
        self.name = name
        self.power = power

    # PROPERTY
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def power(self):
        return self._power

    # SETTERS
    @id.setter
    def id(self, val):
        if val < 0:
            raise ValueError(f'id {self.name} не должен быть отрицательным!')
        self._id = val

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise ValueError('Имя должно быть строкой!')
        self._name = val

    @power.setter
    def power(self, val):
        if val < 0:
            raise ValueError(f'потребляемая мощность {self.name} не должен быть отрицательная!')
        self._power = val


class Printer(OfficeEquipment):

    def __init__(self, id, name, power, ink):
        super().__init__(id, name, power)
        self.ink = ink

    def get_level_ink(self):
        return ''.join([f'Цвет: {color}. Остаток {level} % \n' for color, level in self.ink.items()])

    @property
    def ink(self):
        return self._ink

    @ink.setter
    def ink(self, color):
        tmp_dict = {}
        if isinstance(color, list):
            for cl in color:
                tmp_dict[cl] = 100
            self._ink = tmp_dict
        else:
            tmp_dict[color] = 100
            self._ink = tmp_dict


class Scaner(OfficeEquipment):

    def __init__(self, id, name, power, scan_type):
        super().__init__(id, name, power)
        self.scan_type = scan_type

    @property
    def scan_type(self):
        return self._scan_type

    @scan_type.setter
    def scan_type(self, val):
        if not isinstance(val, str):
            raise ValueError('тип сканера должен быть строкой!')
        self._scan_type = val


class Xerox(OfficeEquipment):
    def __init__(self, id, name, power, xerox_type):
        super(Xerox, self).__init__(id, name, power)
        self.xerox_type = xerox_type

    @property
    def xerox_type(self):
        return self._xerox_type

    @xerox_type.setter
    def xerox_type(self, val):
        if not isinstance(val, str):
            raise ValueError('тип ксерокса должен быть строкой!')
        self._xerox_type = val


if __name__ == '__main__':
    try:
        ofc_1 = OfficeWarehouse(0, 'Арсений')
        printer = Printer(0, 'Epson', 220, ['черный', 'красный', 'желтый'])
        scan = Scaner(0, 'HP', 380, 'построчный')
        xerox = Xerox(0, 'Samsung', 220, 'многофункциональный')
    except Exception as e:
        print(e)

from MyException import EquipmentError


class OfficeEquipment:

    def __init__(self, id, name, power, type):
        try:
            self.id = id
            self.name = name
            self.power = power
            self.type = type
        except EquipmentError as e:
            raise EquipmentError(f'Проблемы с оргтехникой: {e}')

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
            raise EquipmentError(f'id не должен быть отрицательным!')
        self._id = val

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise EquipmentError('Имя должно быть строкой!')
        self._name = val

    @power.setter
    def power(self, val):
        if val < 0:
            raise EquipmentError(f'потребляемая мощность {self.name} не должен быть отрицательная!')
        self._power = val

    def get_type(self):
        return self.type


class Printer(OfficeEquipment):

    def __init__(self, id, name, power, ink):
        try:
            super().__init__(id, name, power, 'Принтер')
            self.ink = ink
        except EquipmentError as e:
            raise EquipmentError(e)

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
        try:
            super().__init__(id, name, power, 'Сканер')
            self.scan_type = scan_type
        except EquipmentError as e:
            raise EquipmentError(e)

    @property
    def scan_type(self):
        return self._scan_type

    @scan_type.setter
    def scan_type(self, val):
        if not isinstance(val, str):
            raise EquipmentError('тип сканера должен быть строкой!')
        self._scan_type = val


class Xerox(OfficeEquipment):
    def __init__(self, id, name, power, xerox_type):
        try:
            super().__init__(id, name, power, 'Ксерокс')
            self.xerox_type = xerox_type
        except EquipmentError as e:
            raise EquipmentError(e)

    @property
    def xerox_type(self):
        return self._xerox_type

    @xerox_type.setter
    def xerox_type(self, val):
        if not isinstance(val, str):
            raise EquipmentError('тип ксерокса должен быть строкой!')
        self._xerox_type = val

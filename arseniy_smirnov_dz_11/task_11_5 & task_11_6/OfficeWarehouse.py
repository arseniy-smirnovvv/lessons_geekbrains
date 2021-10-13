from MyException import WarehouseError


class OfficeWarehouse:
    def __init__(self, num, name_manager):
        try:
            self.num = num
            self.name_manager = name_manager
            self.lst_equipment = {}
        except Exception as e:
            raise WarehouseError(f'Проблемы со складом: {e}')

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
            raise WarehouseError('id склада должно быть числом!')
        if not isinstance(val, (int, float)):
            raise WarehouseError('id склада должен быть числом!')
        if val < 0:
            raise WarehouseError('id склада не должен быть отрицательным!')
        self._num = val

    @name_manager.setter
    def name_manager(self, name):
        if not isinstance(name, str):
            raise WarehouseError('имя менеджера должно быть строкой!')
        self._name_manager = name

    def add_equipment(self, values):
        tmp_dict = {}
        if isinstance(values, list):
            for eq in values:
                if eq.__class__.__base__.__name__ != 'OfficeEquipment':
                    raise WarehouseError('Проблема со складом: неправильный тип данных оргтехники!')
                type_eq = eq.get_type()
                if eq.get_type() not in tmp_dict:
                    tmp_dict[type_eq] = {}
                    tmp_dict[type_eq]['count'] = 1
                    tmp_dict[type_eq]['list'] = [eq]
                else:
                    tmp_dict[type_eq]['count'] = tmp_dict[type_eq]['count'] + 1
                    tmp_dict[type_eq]['list'] = [*tmp_dict[type_eq]['list'], eq]
        else:
            tmp_dict[values.get_type()] = {}
            tmp_dict[values.eq.get_type()]['count'] = 1
            tmp_dict[values.eq.get_type()]['list'] = [values]
        self.lst_equipment = tmp_dict

    def broadcast_equipment(self, new_warehouse):
        try:
            new_warehouse.accept_equipment(self.lst_equipment)
            count = self.get_count_equipment()
            self.lst_equipment = {}
            print(f'Вы успешно переместили {count} на склад с ID {new_warehouse.num}')
        except Exception as e:
            raise WarehouseError(f'Проблемы со складом: {e}')

    def accept_equipment(self, equipment):
        self.lst_equipment = equipment

    def get_count_equipment(self):
        return sum([int(eq['count']) for eq in self.lst_equipment.values()])

    def __str__(self):
        st = f'Номер склада склада: {self.num} \n' \
             f'Менеджер склада: {self.name_manager}\n' \
             '\n'

        for type_name, values in self.lst_equipment.items():
            st += f'Тип техники: {type_name}. Количество на складе: {values["count"]}.\n'
            st += '-' * 10 + '\n'
            for org in values['list']:
                st += f'Название {type_name}: {org.name}\n'
                st += f'Идентификатор устройства: {org.id}\n'
                st += f'Потребляемая мощность: {org.power} \n'
                st += '\n'
        return st

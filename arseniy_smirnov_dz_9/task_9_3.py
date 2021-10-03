class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.positon = position
        self.__income = {'wage': income, 'bonus': 0}

    def set_bonus(self, bonus):
        self.__income['bonus'] = bonus

    def get_income_wage(self):
        return int(self.__income['wage'])

    def get_income_bonus(self):
        return int(self.__income['bonus'])

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname


class Position(Worker):

    def get_full_name(self):
        return f'{self.get_name()} {self.get_surname()}'

    def get_total_income(self):
        return self.get_income_wage() + self.get_income_bonus()

manager = Position('Арсений', 'Смирнов', 'Менеджер по продажам', 30000)
print(manager.get_full_name())
print(manager.get_total_income())
manager.set_bonus(10000)
print(manager.get_total_income())
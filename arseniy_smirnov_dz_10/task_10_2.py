from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value <= 0:
            self._value = 1
        else:
            self._value = value

    @abstractmethod
    def get_calculation(self):
        pass


class Coat(Clothes):

    def get_calculation(self):
        return round(self.value / 6.5 + 0.5, 2)


class Costume(Clothes):

    def get_calculation(self):
        return 2 * self.value + 0.3


coat = Coat(187)
costume = Costume(54)
print(f'Для пальто нужно: {coat.get_calculation()}')
print(f'Для костюма нужно: {costume.get_calculation()}')
print(Coat(-142).get_calculation())

class Car:
    __go = False
    __stop = True
    __turn = 'stop'

    def __init__(self, speed, color, name, is_police=False):
        self.__speed = speed
        self.__color = color
        self.__name = name
        self.__is_police = is_police

    def get_police(self):
        return self.__is_police

    def set_police(self, bool):
        self.__is_police = bool

    def get_speed(self):
        return self.__speed

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

    def show_speed(self):
        print(self.get_speed())

    def get_go(self):
        return self.__go

    def get_stop(self):
        return self.__stop

    def get_turn(self):
        return self.__turn

    def check_police_car(self):
        return self.__is_police

    def set_stop(self, bool):
        self.__stop = bool

    def set_go(self, bool):
        self.__go = bool

    def go(self):
        self.set_go(True)
        self.set_stop(False)
        self.turn('прямо')

    def turn(self, direction):
        self.__turn = direction

    def info(self):
        res = (f'Марка машины: {self.get_name()}\n' +
               f'Цвет машины: {self.get_color()}\n' +
               f'Скорость машины {self.get_speed()}\n'
               )
        if self.get_go():
            res += f'Машина едет в направление {self.get_turn()}\n'
        else:
            res += f'Машина стоит на месте\n'
        if self.get_police():
            res += f'Это полицейская машина\n'
        return res


class SportCar(Car):
    pass


class TownCar(Car):

    def show_speed(self):
        if self.get_speed() > 60:
            print('Скорость транспортного средства превышает 60 км в час!')


class WorkCar(Car):

    def show_speed(self):
        if self.get_speed() > 40:
            print('Скорость транспортного средства превышает 40 км в час!')


class PoliceCar(Car):
    pass


town_car = TownCar(100, 'red', 'Skoda')
sport_car = SportCar(120, 'yellow', 'Audi')
work_car = WorkCar(80, 'black', 'Hundai')
police_car = Car(140, 'white', 'Ваз 2107', is_police=True)


town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()

print()
print(police_car.info())
police_car.go()
police_car.turn('налево')
print(police_car.info())
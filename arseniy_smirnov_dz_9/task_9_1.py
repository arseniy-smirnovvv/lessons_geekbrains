import time


class TrafficLignt:

    def __init__(self, green_second):
        self.__color = {'Красный': 7, 'Желтый': 2, 'Зеленый': green_second}

    def get_color(self):
        return self.__color

    def running(self, count=10):
        while count:
            for color, second in self.get_color().items():
                print(f'Загорелся {color} цвет.')
                time.sleep(second)
            count -= 1
        return True

    def __del__(self):
        print('Карамба! Светофор снес какой-то сборщик мусора!')

t_l = TrafficLignt(2)
t_l.running(1)



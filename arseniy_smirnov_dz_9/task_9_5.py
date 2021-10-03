class Stationery:
    def __init__(self, title):
        self.__title = title

    def get_titile(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def draw(self):
        print(f'Запуск отрисовки {self.get_titile()}')


class Pen(Stationery):
    def draw(self):
        print('Запуск рисовки ручки')


class Handle(Stationery):
    def draw(self):
        print('Запуск нанесения маркера')


x = Stationery('предмет какой-то')
pen = Pen('Ручка')
handle = Handle('Маркер')

x.draw()
pen.draw()
handle.draw()
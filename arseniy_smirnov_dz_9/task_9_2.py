class Road:
    __weight = 25
    __thickness = 5
    __black_square = '■'

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_weight(self):
        return self.__weight

    def get_thickness(self):
        return self.__thickness

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def mass_calculation(self):
        return f'{(self.get_length() * self.get_width() * self.get_weight() * self.get_thickness()) // 1000} т.'

    def print_road(self):
        length = self.get_length()
        width = self.get_width()
        for l in range(length):
            print()
            for w in range(width):
                print(self.__black_square, end='')
        print()

road_1 = Road(50, 5)
road_1.print_road()
print(f'Вот такая дорога получится, ну а для того что бы её сделать нам нужно {road_1.mass_calculation()} асфальта')

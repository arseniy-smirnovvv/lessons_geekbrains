class Cell:

    def __init__(self, count_cell):
        self.count_cell = count_cell

    @property
    def count_cell(self):
        return self.__count_cell

    @count_cell.setter
    def count_cell(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError('Количество клеток должно быть целым числом!')
        if isinstance(val, float):
            self.__count_cell = int(val)
        else:
            self.__count_cell = val

    def __str__(self):
        return str(self.__count_cell)

    def __add__(self, other):
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        if (self.count_cell - other.count_cell) > 0:
            return Cell(self.count_cell - other.count_cell)
        else:
            raise ArithmeticError('Разность двух клеток не может быть меньше нуля!')

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __floordiv__(self, other):
        return Cell(self.count_cell // other.count_cell)

    def __truediv__(self, other):
        return Cell(self.count_cell // other.count_cell)

    def make_order(self, example):
        res = ''
        i = 0
        for _ in range(example.count_cell):
            if i == 5:
                res += '\n'
                i = 0
            res += '*'
            i += 1
        return res


try:
    cl_1 = Cell(4)
    cl_2 = Cell(2)
    cl_3 = (cl_1 + cl_2)
    print(cl_3)
    print(cl_1 - cl_2)
    print(cl_1 * cl_2)
    print(cl_1 / cl_2)
    print(cl_1 // cl_2)
    print(cl_3.make_order(cl_3))
except Exception as e:
    print(e)

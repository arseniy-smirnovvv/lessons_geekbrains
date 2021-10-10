class Matrix:

    def __init__(self, mt):
        self.array = mt

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, val):
        # Проверка на то, что принимаемый аргумент был списком
        # или что бы все элементы спика должны быть списками
        if not isinstance(val, list) \
                or len(val) == 0 \
                or not all([True if isinstance(el, list) else None for el in val]):
            raise ValueError('матрица должна состояить из списка списков!')

        # Проверяем что бы все списки в списке должны быть одинаковой длины
        if len(set([len(el) for el in val])) > 1:
            raise Exception('все списки должны бить одинаковыми по размеру!')

        # Проверяем на то, что бы каждый элемент матрицы был числом
        for ls in val:
            if not all([True if isinstance(el, (int, float)) else None for el in ls]):
                raise ValueError('каждый элемент матрицы должен быть числом!')
        self._array = val

    def __str__(self):
        res = ''
        for ls in self.array:
            for el in ls:
                res += f'{el} '
            res += '\n'
        return res[:-1]

    def __add__(self, other):
        if len(self.array) != len(other.array):
            raise Exception('длина матриц должна быть одинаковой!')
        res_mt = []
        i = -1
        for mt_1, mt_2 in zip(self.array, other.array):
            i += 1
            res_mt.append([])
            for val_1, val_2 in zip(mt_1, mt_2):
                res_mt[i].append(val_1 + val_2)

        return Matrix(res_mt)
try:
    mt_1 = Matrix([[1, 2, 3], [21, 5, 6], [1, 6, 4]])
    mt_2 = Matrix([[5, 1, 6], [8, 2, 1], [4, 1, 6]])
    print('первая матрица: ')
    print(mt_1)
    print('вторая матрица: ')
    print(mt_2)
    print('их сумма: ')
    print(mt_1 + mt_2)
except Exception as e:
    print(e)

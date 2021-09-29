def type_logger(func):
    def wrapper(*args):
        res = func(*args)
        [print(f'{func.__name__} ({arg}: {type(arg)})') for arg in args]
        return res
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

@type_logger
def sum_num(x, y):
    return x + y

a = calc_cube(3)
b = sum_num(1, 2)
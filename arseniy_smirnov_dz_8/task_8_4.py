def val_checker(check_func):
    def decor(func):
        def wrapper(*args):
            if not check_func(*args):
                raise ValueError(f'неправильное значение: {args[0]}')
            res = func(*args)
            return res
        return wrapper
    return decor


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

try:
    print(calc_cube(3))
    print(calc_cube(-3))
except ValueError as e:
    print(e)
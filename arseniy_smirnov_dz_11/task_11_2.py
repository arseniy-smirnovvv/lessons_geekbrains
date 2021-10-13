class NoZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


class Numeric:
    def __init__(self, n):
        self.n = n

    def __truediv__(self, other):
        if other.n == 0:
            raise NoZeroDivision('Нельзя делить на ноль!')
        return Numeric(self.n + other.n)

    def __str__(self):
        return int(self.n)


a = Numeric(10)
b = Numeric(0)

try:
    c = a / b
except Exception as e:
    print(e)
    print(type(e).__name__)


try:
    c = a / b
except NoZeroDivision as e:
    print(e)
    print(type(e).__name__)


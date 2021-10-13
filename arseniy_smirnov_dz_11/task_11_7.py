class ComplexNum:

    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return ComplexNum(self.n + other.n)

    def __mul__(self, other):
        return ComplexNum(self.n * other.n)

    def __str__(self):
        return str(self.n)

a = ComplexNum(1 + 2j)
b = ComplexNum(2 + 3j)
print(a + b)
print(a * b)

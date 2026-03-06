"""
Write a class ‘Complex’ to represent complex numbers, along with overloaded
operators ‘+’ and ‘*’ which adds and multiplies them.
"""


class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return f"{self.r} + {self.i}i"

    def __add__(self, second):
        return Complex(self.r + second.r, self.i + second.i)

    def __mul__(self, second):
        return Complex((self.r * second.r) - (self.i * second.i), (self.r * second.i) + (second.r * self.i))


c1 = Complex(1, 2)
c2 = Complex(3, 4)

c3 = c1 + c2
c4 = c1 * c2

print(c3)
print(c4)

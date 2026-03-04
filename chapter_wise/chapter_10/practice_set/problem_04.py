"""
Add a static method in problem 2, to greet the user with hello.
"""


class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"Square of {self.number} = {self.number*self.number}")

    def cube(self):
        print(f"Cube of {self.number} = {self.number*self.number*self.number}")

    def sq_root(self):
        print(f"Square Root of {self.number} = {self.number**1/2}")

    @staticmethod
    def hello():
        print("Hello there")


cal_1 = Calculator(24)

cal_1.square()
cal_1.cube()
cal_1.sq_root()
cal_1.hello()

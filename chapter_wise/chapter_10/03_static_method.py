"""
In order to use static methods that does'nt need to use attribute and methods of the instance there is no need to use self there so in that case we use @staticmethod decorator with that method
"""


class Employee:
    name = "Muhammad Tayyab"
    role = "Web Developer"
    salary = 400000

    @staticmethod
    def greeting():
        print("Hello World")


emp_1 = Employee()

emp_1.greeting()

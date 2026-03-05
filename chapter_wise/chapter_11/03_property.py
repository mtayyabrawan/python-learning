"""
Property decorator is used to define attribute using methods
"""


class Student:

    def __init__(self, name):
        # the attribute starting with double underscore will be private in classes
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


st1 = Student("Muhammad Tayyab")
print(st1.name)
st1.name = "Tayyab Raza"
print(st1.name)
del st1.name  # del deletes the attribute or method of the object
print(st1.name)

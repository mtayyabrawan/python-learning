"""
We can overload the operotors in class and is called as polymorphism
"""


class String():
    def __init__(self, s):
        self.__s = s

    def __add__(self, b):
        return len(self.__s) + len(b.__s)


str1 = String("222")
str2 = String("shshs")
print(str1+str2)

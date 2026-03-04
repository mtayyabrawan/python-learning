"""
Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute? No
"""


class Demo():
    a = "a"


obj = Demo()

print(obj.a)
obj.a = "o"
print(obj.a)

print(Demo.a)

"""
Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
‘Pets’. Add a method ‘bark’ to class ‘Dog’.
"""


class Animal:
    pass


class Pet(Animal):
    pass


class Dog(Pet):
    @staticmethod
    def bark():
        print("Woof Woof Woof!")


puppy = Dog()

puppy.bark()

"""
Constructors are special methods of classes. They execute whenever new instance of that class is instantiated the are defined by using __init__ keyword
"""


class Employee:
    name = "Muhammad Tayyab"
    role = "Web Developer"
    salary = 400000

    @staticmethod
    def __init__():
        print("New instance of Employee is created")


emp_1 = Employee()
emp_2 = Employee()

# we can also pass custom parameters to the constructor for different use


class Student:
    def __init__(self, name, roll_no, marks, course):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.course = course

    def get_student_info(self):
        print(
            f"Name: {self.name}\nRoll No: {self.roll_no}\nMarks: {self.marks}\nCourse: {self.course}")


tayyab = Student("Muhammad Tayyab", 2103508, 94, "Computer Science")

tayyab.get_student_info()

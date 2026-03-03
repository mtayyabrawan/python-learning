"""
OOP: Class is the blueprint on which other objects are created like e.g
Like Empty Application Form is a class
whe someone fills it now it becomes object of of that class
Class contains attributes and methods
"""


class Employee:
    name = "Muhammad Tayyab"
    role = "Web Developer"
    salary = 400000


# employee_1 is the object of class Employee ans also called as instance of Employee
employee_1 = Employee()

# two types of attributes class & object specific

print(Employee.name)  # class attribute
print(employee_1.name)  # object attribute

# both can be changed but object attributes have more preference on class attributes

Employee.name = "Tayyab Raza"
employee_1.name = "Tayyab Raza"

print(employee_1.name)

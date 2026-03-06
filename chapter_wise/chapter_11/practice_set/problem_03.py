"""
Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
which changes the value of increment based on the salary.
"""


class Employee:
    def __init__(self, salary, increment):
        self.__salary = salary
        self.__increment = increment

    @property
    def salary_after_increment(self):
        self.__salary += self.__increment
        return self.__salary

    @salary_after_increment.setter
    def salary_after_increment(self, value):
        self.__salary += value
        return self.__salary


e1 = Employee(120000, 5000)

print(e1.salary_after_increment)
e1.salary_after_increment = 12000
print(e1.salary_after_increment)

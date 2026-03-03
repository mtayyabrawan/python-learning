"""
It represents the instance of the class automatically present in all methods of classes
"""


class Employee:
    name = "Muhammad Tayyab"
    role = "Web Developer"
    salary = 400000

    def get_info(self):  # self is used whenever we need to use attributes and methods
        # print(f"Name: {name}\nRole: {role}\nSalary: {salary}") # by directly using attribute names will not work so the self keyword is used that contains all current instance attributes and methods
        print("self is already there")
        print(f"Name: {self.name}\nRole: {self.name}\nSalary: {self.name}")


emp_1 = Employee()

emp_1.get_info()  # self is already passed in this case to the method

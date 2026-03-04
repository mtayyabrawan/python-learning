"""
Create a class “Programmer” for storing information of few programmers
working at Microsoft.
"""


from logging import info


class Programmer:
    name = None
    language = None
    salary = None
    company = "Microsoft"

    def __init__(self, name, language, salary=1000000):
        self.name = name
        self.language = language
        self.salary = salary

    def info(self):
        print(
            f"Name: {self.name}\nLanguage: {self.language}\nSalary: {self.salary}\nCompany: {self.company}")
        return self.name, self.language, self.salary, self.company

    def update_info(self, name, language, salary, company):
        self.name = name
        self.language = language
        self.salary = salary
        self.company = company
        print(f"Student info updated of {name}")


tayyab = Programmer("Muhammad Tayyab", "JavaScript")

tayyab.info()

tayyab.update_info(name="Tayyab", language="Python",
                   salary=1500000, company="GitHub")

print(tayyab.info())

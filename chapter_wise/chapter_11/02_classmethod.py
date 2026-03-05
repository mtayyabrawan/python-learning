"""
Class Method is use to update acces drectly the class attributes
"""

class Demo:
    college_name = "Punjab College"

    def info(self):
        print(f"College Name: {self.college_name}")

    @classmethod
    def default_college(cls):
        print(f"Default College Name: {cls.college_name}")


d1 = Demo()
d1.info()
d1.college_name = "Oxford College"
d1.info()
d1.default_college()
Demo.college_name = "Superior College"
d1.default_college()

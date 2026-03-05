"""
Inheritance means copying attribute of a class to the second one
The class from which these attributes and methods are taken is known as parent or base class
and the class which tokes attributes and methods from other class is known as child or derived class
"""


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def info(self):
        print(f"Book Name: {self.name}\nAuthor Name: {self.author}")


class BookTranslation(Book):
    def __init__(self, name, author, translated_by, language):
        super().__init__(name, author)  # super() is used to call parent class constructor
        self.translated_by = translated_by
        self.language = language

    def info_t(self):
        print(
            f"{self.language} Translation\nTranslated By: {self.translated_by}")


b1 = Book("Tareek ul Khulafa", "Jalaludin Sayuti")
tb1 = BookTranslation("Tareek ul Khulafa",
                      "Jalaludin Sayuti", "Muhammad Tayyab", "English")

b1.info()
tb1.info()
tb1.info_t()

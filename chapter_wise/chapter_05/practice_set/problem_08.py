"""
If languages of two friends are same; what will happen to the program in problem
6? The language is stored as it is
"""

preference_dict = {}

f_name = input("Enter friend 1 name : ")
f_lang = input("Enter friend 1 fav lang : ")

preference_dict.update({f_name: f_lang})

f_name = input("Enter friend 2 name : ")
f_lang = input("Enter friend 2 fav lang : ")

preference_dict.update({f_name: f_lang})

f_name = input("Enter friend 3 name : ")
f_lang = input("Enter friend 3 fav lang : ")

preference_dict.update({f_name: f_lang})

f_name = input("Enter friend 4 name : ")
f_lang = input("Enter friend 4 fav lang : ")

preference_dict.update({f_name: f_lang})

print(preference_dict)

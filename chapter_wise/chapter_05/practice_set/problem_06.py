"""
Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
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

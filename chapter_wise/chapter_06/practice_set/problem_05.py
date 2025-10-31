"""
Write a program which finds out whether a given name is present in a list or not.
"""

names = ["muhammad tayyab", "talha", "awais", "khubaib", "zain"]

user_inp = input("Enter name : ").lower()

if user_inp in names:
    print("Your name present in our system")
else:
    print("Sorry! name not found")

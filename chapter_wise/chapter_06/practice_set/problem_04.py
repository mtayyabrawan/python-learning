"""
Write a program to find whether a given username contains less than 10
characters or not.
"""

username = input("Please enter username : ")

if len(username) < 10:
    print("Valid username")
else:
    print("Invalid username")

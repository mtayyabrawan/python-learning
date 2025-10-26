"""
Input (input) is used to get input from user
always return the value provided by the user as a string
"""

name = input("Enter your name here : ")

print(f"Welcome {name}! to Pyverse")

age = int(input("Enter your age : "))

print(f"You are an adult : {age > 18}")
"""
Write a program to print multiplication table of a given number using for loop.
"""

number = int(input("Enter your table number: "))

for num in range(1, 11):
    print(f"{number} X {num} = {number * num}")

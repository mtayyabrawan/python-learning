"""
Write a program to calculate the factorial of a given number using for loop.
"""

number = int(input("Enter your number to calculate factorial: "))

factorial = 1
for num in range(1, number + 1):
    factorial *= num
else:
    print(f"Factorial of {number}! = {factorial}")

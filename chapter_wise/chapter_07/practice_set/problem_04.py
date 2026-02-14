"""
Write a program to find whether a given number is prime or not.
"""

number = int(input("Enter your number to check is it prime or not: "))

for num in range(2, number):
    if number % num == 0:
        print(f"{number} is not a prime number")
        break
else:
    print(f"{number} is a prime number")

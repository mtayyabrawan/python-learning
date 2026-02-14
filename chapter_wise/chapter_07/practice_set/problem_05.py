"""
Write a program to find the sum of first n natural numbers using while loop.
"""

number = int(input("Enter any natural number: "))

sum = 0
idx = 1

while idx <= number:
    sum += idx
    idx += 1
else:
    print(f"Sum of all natural number till {number} = {sum}")

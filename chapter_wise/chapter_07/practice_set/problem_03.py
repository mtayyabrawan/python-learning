"""
Attempt problem 1 using while loop
"""

number = int(input("Enter your table number: "))

num = 1

while num <= 10:
    print(f"{number} X {num} = {number * num}")
    num += 1

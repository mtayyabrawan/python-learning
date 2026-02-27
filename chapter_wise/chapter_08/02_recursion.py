"""
Recursion is the function that calls it self and works same as loops works
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter number : "))

print(f"Factorial of {num} = {factorial(num)}")

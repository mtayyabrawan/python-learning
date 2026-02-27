"""
Write a recursive function to calculate the sum of first n natural numbers.
"""


def nature_sum(n):
    if n == 1 or n <= 0:
        return 1
    return n + nature_sum(n - 1)


num = int(input("Enter number: "))

print(f"Sum of first {num} natural numbers = {nature_sum(num)}")

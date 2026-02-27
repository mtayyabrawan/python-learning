"""
 Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
"""


def reverse_pattern(n):
    while n >= 1:
        print("*" * n)
        n -= 1


num = int(input("Enter number: "))

reverse_pattern(num)

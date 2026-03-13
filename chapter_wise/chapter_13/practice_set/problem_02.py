"""
Write a program to find the maximum of the numbers in a list using the reduce
function.
"""

from functools import reduce


l = [1, 2, 3, 4, 5]
maximum = reduce(lambda x, y: x if x > y else y, l)
print(maximum)

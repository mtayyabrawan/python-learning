"""
Write a program to print the following star pattern:
*
**
*** for n = 3
"""

n = 3

for i in range(1, n + 1):
    for k in range(i):
        print("*", end="")
    print("\n")

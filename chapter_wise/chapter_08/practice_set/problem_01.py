"""
Write a program using functions to find greatest of three numbers.
"""


def greatest_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num1 and num2 > num2:
        return num2
    if num3 > num1 and num3 > num2:
        return num3


num1 = int(input("Enter 1st number  : "))
num2 = int(input("Enter 2nd number  : "))
num3 = int(input("Enter 3rd number  : "))

print(
    f"{greatest_num(num1,num2,num3)} is the greatest number from {num1}, {num2}, {num3}"
)

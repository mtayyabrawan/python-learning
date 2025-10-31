"""
Write a program to find the greatest of four numbers entered by the user.
"""

nums_by_user = []

nums_by_user.append(int(input("Enter first number : ")))
nums_by_user.append(int(input("Enter second number : ")))
nums_by_user.append(int(input("Enter third number : ")))
nums_by_user.append(int(input("Enter fourth number : ")))

if (
    nums_by_user[0] > nums_by_user[1]
    and nums_by_user[0] > nums_by_user[2]
    and nums_by_user[0] > nums_by_user[3]
):
    print(f"{nums_by_user[0]} is the greatest number")
elif (
    nums_by_user[1] > nums_by_user[0]
    and nums_by_user[1] > nums_by_user[2]
    and nums_by_user[1] > nums_by_user[3]
):
    print(f"{nums_by_user[1]} is the greatest number")
elif (
    nums_by_user[2] > nums_by_user[0]
    and nums_by_user[2] > nums_by_user[1]
    and nums_by_user[2] > nums_by_user[3]
):
    print(f"{nums_by_user[2]} is the greatest number")
else:
    print(f"{nums_by_user[3]} is the greatest number")

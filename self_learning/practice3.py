# grading system
marks = int(input("Enter your marks : "))

if marks >= 90:
    print("Your grade is : A")
elif marks >= 80:
    print("Your grade is : B")
elif marks >= 70:
    print("Your grade is : C")
else:
    print("Your grade is : D")
 # checking odd or even

num = int(input("Enter a number : "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# check greater of three nums

num1, num2, num3 = int(input("Enter first num : ")), int(
    input("Enter second num : ")), int(input("Enter third num : "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

# check if num is multiple of 7 or not

num = int(input('Enter number to check multiple of 7:'))

if num % 7 == 0:
    print(f"{num} is multiple of 7")
else:
    print(f"{num} is not multiple of 7")

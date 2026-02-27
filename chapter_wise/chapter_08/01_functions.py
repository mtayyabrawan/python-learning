"""
Functions: are the block of code to perform a specific tasks
There are 2 type of functions:
Built in : That comes with python itself like print(), len(), range(), type() etc.
User defined : These are defined by user it self we can also define multiple funtions
"""


def avg():  # just defining the functions does'nt work we have to call them
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    avg = (a + b + c) / 3
    print(f"Average of {a}, {b}, {c} = {avg}")


avg()  # function call

# Quick Quiz: Write a program to greet a user with “Good day” using functions.


def greet():
    print("Good day")


greet()

# Arguments:

# To performe more usefull tasks we can also pass arguments to the functions while defining the function in parantheses.


def avg2(numbers_list):
    sum = 0
    for num in numbers_list:
        sum += num
    avg = sum / len(numbers_list)
    print(f"Average of {numbers_list} = {avg}")


num_l = [45, 78, 34, 90, 23, 18, 49]

avg2(num_l)

# Return value: like we can give arguments to the fucntions in return we can also get somevalues from funcs as return value, in this we can use these value for other tasks and calculations


def avg3(numbers_list):
    sum = 0
    for num in numbers_list:
        sum += num
    return sum / len(numbers_list)


print(f"Average of {num_l} is {avg3(num_l)}")

# Default paramenters: are those arguments of the functions whose values are already defined while defining the function so if user does'nt gives that parameter's value then the default value will be used


def multiplication_table(num, times=10):  # here default parameter is times = 10
    for i in range(1, times + 1):
        print(f"{num} X {i} = {num*i}")


multiplication_table(
    4
)  # here we have not given second value for times parameter so here default parameter value is used

multiplication_table(5, 15)  # here we have given value for times so that is used

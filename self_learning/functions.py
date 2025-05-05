# defining functions
def Sum(a, b, c):
    return a + b + c


# calling function
print(Sum(8, 9, 7))


# function with default values
def avg(a=9, b=4, c=2):
    return Sum(a, b, c) / 3


print(avg(1))  # calling function with single argument
print(avg(b=1))  # calling function with single but specific parameter

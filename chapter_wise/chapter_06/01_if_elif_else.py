"""
Conditionals: if, elif, else
"""

num = 22

if num % 2 == 0:  # if condition returns true then the block next to it will be executed
    print(f"{num} is an even number")
else:  # if all the above conditions does'nt meet then this final conditional block is executed
    print(f"{num} is odd number")

# in case we have multiple conditions to check with then wo use elif cluase

age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible for casting vote")
elif age <= 0:
    print("You are entering wrong age please enter your correct age")
else:
    print("You can't cast vote as of now")

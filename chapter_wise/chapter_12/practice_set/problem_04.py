"""
Store the multiplication tables generated in problem 3 in a file named Tables.txt.
"""

num = int(input("Enter number: "))

table = [f"{num} x {i} = {num * i}" for i in range(1,11)]

with open(f"table{num}.txt","w") as file:
    file.write("\n".join(table))
"""
Loops are used to repeat execution of a code for certain conditions
"""

# for loop

for i in range(5):  # range method returns object of given range
    print(i + 1)


for i in range(1, 11):  # by default range start is 0
    print(i)

for i in range(
    1, 11, 2
):  # we can also give steps to jump like we did in slicing lists and strings
    print(i)

l = ["Tayyab", "Muhammad", "Raza", "Ali", "Ahmed", "Abbas", "Haider"]

for name in l:  # prints all the items of list
    print(name)

for idx, value in enumerate(
    l
):  # enamurate returns the list of tupples of eah list items as index and value pair
    print(idx, value)

my_name = "Muhammad Tayyab Raza Awan"

for char in my_name:  # we can also iterate over strings using loops
    print(char, end=", ")
else:  # else executes imediatly after completing loop
    print("\n")


# while loop

idx = 0

while (
    idx < 50
):  # in whilw loop we have to explicitly update the condition inside loop block other wise loop becomes infinite loop
    print(idx)
    idx += 1

i = 0
while i < len(l):
    print(l[i])
    i += 1

# break statement : used to exist loop explicitly

for name in l:
    if name == "Ali":  # exists the loop when name value becomes "Ali"
        break
    print(f"Name: {name}")

for name in l:
    if name == "Ali":  # skips the iteration when name value becomes "Ali"
        continue
    print(f"Name: {name}")

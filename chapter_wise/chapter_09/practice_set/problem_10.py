"""
Write a program to wipe out the content of a file using python.
"""
# method 1
# with open("wipe_file.txt", "w"):
#     pass

# method 2
with open("wipe_file.txt", "w") as file:
    file.write("")

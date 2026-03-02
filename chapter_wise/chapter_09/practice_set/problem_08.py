"""
Write a program to make a copy of a text file “this. txt”
"""

with open("this.txt") as file_1:
    file_1_content = file_1.read()
with open("this_copy.txt", "w") as file2:
    file2.write(file_1_content)

"""
File I/O are built-in functions for files manipulations
"""

# Open function open file with provided name in reading mode
file = open("file.txt", "r")

# print(file.read())  # reads the whole content of file

# print(file.readlines())  # returns the list of lines in the file

print(file.readline())  # reads each line of the file one by one

file.close()

# Writing mode: in this mode if file is present it content will be overwritten with new one if we are writing

new_file = open("my_file.txt", "w")

new_file.write("This file is created by the python project")

new_file.close()

with open("my_file.txt", "a") as append_file:  # using 'with' automatically closes opened file
    append_file.writelines(["This is line one appended",
                           "\nThis is line two appended", "\nThis is line three appended", "\nThis is line four appended"])

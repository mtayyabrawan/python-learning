import os

# opening file for writing
file = open("sample.txt", "w")
# file = open("sample.txt", "a") # for appending

file.write("Hi my name is Muhammad Tayyab Raza Awan")

file.close()
# reading lines of file

file2 = open("sample.txt", "r")

print(file2.readlines())


file2.close()

# using with syntax

with open("demo.txt", "a") as demoFile:
    demoFile.write("This is demo file created using with syntax")
    demoFile.close()

# deleting files


os.remove("demo.txt")
os.remove("sample.txt")

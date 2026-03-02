"""
Write a program to find out whether a file is identical & matches the content of
another file.
"""
with open("this.txt") as file_1:
    file_1_content = file_1.read()
with open("this_copy.txt",) as file_2:
    file_2_content = file_2.read()

if (file_1_content == file_2_content):
    print("These files are identical")
else:
    print("These files are not identical")

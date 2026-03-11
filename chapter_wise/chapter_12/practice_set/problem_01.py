"""
Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
present, a message without exiting the program must be printed prompting the same.
"""

try:
    with open("f1.txt") as f1:
        pass
except Exception as e:
    print(e)

try:
    with open("f2.txt") as f2:
        pass
except Exception as e:
    print(e)
    
try:
    with open("f3.txt") as f3:
        pass
except Exception as e:
    print(e)

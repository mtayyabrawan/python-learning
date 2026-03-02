"""
Write a program to find out the line number where python is present from ques 6.
"""

word = "python"

with open("log.txt") as log_file:
    content = log_file.readlines()

for (idx, val) in enumerate(content):
    if (word.lower() in val.lower()):
        print(f"'{word}' is present in log file at line number {idx+1}")
        break
else:
    print(f"'{word}' is not present in log file")

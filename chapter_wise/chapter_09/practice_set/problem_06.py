"""
Write a program to mine a log file and find out whether it contains ‘python’
"""

word = "python"

with open("log.txt") as log_file:
    content = log_file.read()

if(word.lower() in content.lower()):
    print(f"'{word}' is present in log file")
else:
    print(f"'{word}' is not present in log file")

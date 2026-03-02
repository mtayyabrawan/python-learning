"""
A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file.
"""

word = "Donkey"

with open("donkey_file.txt", "r") as donkey_file:
    content = donkey_file.read().replace("donkey", "#####").replace("Donkey", "#####")
with open("donkey_file.txt", "w") as donkey_file:
    donkey_file.write(content)

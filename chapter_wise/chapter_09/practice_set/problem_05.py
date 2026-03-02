"""
Repeat program 4 for a list of such words to be censored.
"""
words = ["donkey", "people", "eaten"]

with open("donkey_file.txt", "r") as donkey_file:
    content = donkey_file.read()
    for word in words:
        content = content.replace(word.lower(), "#####").replace(
            word.capitalize(), "#####")
with open("donkey_file.txt", "w") as donkey_file:
    donkey_file.write(content)

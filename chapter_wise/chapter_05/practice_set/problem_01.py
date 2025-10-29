"""
Write a program to create a dictionary of Urdu words with values as their English
translation. Provide user with an option to look it up!
"""

dictionary = {"Kitab": "Book", "Gari": "Car", "Golli": "Bullet", "Qalam": "Pen"}

word = (
    input(f"Enter your word from these to get translation : {list(dictionary.keys())} ")
    .strip()
    .capitalize()
)

print(f"{word} means {dictionary.get(word)} in English")

"""
Write a program to read the text from a given file ‘poem.txt’ and find out
whether it contains the word ‘twinkle’.
"""

with open("poem.txt") as poem_file:
    poem = poem_file.read()
    if ("twinkle" in poem):
        print("Yes Poem contain 'twinkle' word")
    else:
        print("No Poem does'nt contain 'twinkle' word")

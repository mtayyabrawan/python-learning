"""
There are menay methods related to strings to manipulate strings
"""

str = "The quick brown fox jumps over the lazy dog"

print(len(str))  # prints the length of string (how many characters are in the string)

print(
    str.endswith("lazy")
)  # gives boolean whether string is ending with the given string or not we can also pass start or end position for that function default includes whole string

print(
    str.index("the")
)  # prints the lowest index of given string in the string if found and error if not found

print(str.find("to"))  # works simmilar to .index() but returns -1 on failure

capital_str = str[4:].capitalize()
lower_str = str.lower()
upper_str = str.upper()
title_str = str.title()

print(capital_str)
print(lower_str)
print(upper_str)
print(title_str)

print(
    str.isalpha()
)  # prints only True if strings only contain alphabets not numbers symbols and spaces

print(
    str.replace("dog", "cat")
)  # replace all occurances of s substring with given string

# There are many other string related methods

# Escape sequence characters are characters that allows some special chars in strings

# \n \t \' \\

print(str.replace(" ", "\n\t"))

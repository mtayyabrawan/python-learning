"""
Dictionaries are also the collections used in pyhon to store data in key value pairs , they are mutable like lists
"""

marks = {
    "tayyab": [56, 89, 67, 40],
    "talha": [78, 94, 73, 47],
    "bilal": [80, 86, 75, 45],
    1: "Muhammad Tayyab Raza Awan",
}

print(marks, type(marks))

# to get values we can't use index like lists in dicts we use Keys

print(marks["tayyab"])  # this throws error if we provide invalid key
print(marks.get("tayyab"))  # this return None if we provide invalid key

marks["tayyab"] = [65, 90, 71, 43]

print(marks)

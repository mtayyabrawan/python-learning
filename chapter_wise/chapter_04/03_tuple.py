"""
Tuples are the structures that contains one or more values similar to list but they are immutable unlike lists
"""

marks = (45, 89, 73, 64, 58, 49)

print(marks)
print(type(marks))

empty_tup = ("Tayyab",)  # to defied tuple with single value use (value,)

print(empty_tup)
print(type(empty_tup))

print(marks[5])

# slicing works same as on string and lists

print(marks[2:5])

# unpacking tuple

a, b, c, d, e, f = marks

print(a, b, c)

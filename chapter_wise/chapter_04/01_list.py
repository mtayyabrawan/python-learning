"""
Lists (arrays) are the collection of data of one or more types
there are two ways for defining lists
Lists are mutable
"""

student_info = ["Muhammad Tayyab", "Python Course", 184, "Online"]
another_list = list(["Muhammad Tayyab", "Abdullah", "Talha", "Awais"])

# we can get values of list by passing index

print(student_info)  # prints whole string
print(student_info[3])
print(student_info[1])  # getting value that is not present throws error
print(type(student_info))
print(type(another_list))

# SLicing: list slicing works same as string slicing

print(another_list[2:4])  # slicing does't mutates the lists

print(student_info[:2])

student_info[0] = "Muhammad Tayyab Raza Awan"  # mutating value at index 0

print(student_info)

# list concatination and multiplication:

concat_list = student_info + another_list

print(concat_list)

multiplied = student_info * 2

print(multiplied)
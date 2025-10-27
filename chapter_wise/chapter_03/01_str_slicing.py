"""
Strings: are the combination of characters including symnols letters and numbers they are defined in three different ways
Strings are immutables means that they are not changeable by working with methods but we can reassign them values
"""

name = "Muhammad Tayyab"
first_name = "Muhammad"
last_name = """Tayyab"""

# to get single character of string we can get them as

print(last_name[4])

# slicing : slicing is the technique of cutting string to small pieces

first_4_cars = name[
    0:4
]  # Syntax : variable_name[index_to_start_slicing:index_to_which_slice] the last index character is not included in sliced string

print(first_4_cars)


# Negative slicing : as indexes in python starts from 0 so negative index means counting from the end let's assume if you have to get -5 character of string then you can calculate it as len(that_string) - 5

print(last_name[-5:5])  # prints ayya is also equals
print(last_name[len(last_name) - 5 : 5])  # this also prints ayya

# default behaviours

print(last_name[:3])  # by default if start index is not given then it starts from 0
print(
    last_name[2:]
)  # by default if end index is not given then it ends at length of that string
print(
    last_name[:]
)  # by default if both indexs are not given then prints the whole string as it is

# Skipping characters while slicing

# we can skip characters during slicing by give number of characters to skipp after the last_index as:

print(
    name[3:12:2]
)  # this starts from first_charcter and on 2 index forward to the first_index it prints it

"""
List related methods
"""

fruits = [
    "Apple",
    "Orange",
    "Banana",
    "Grapes",
    "Mango",
    "Guava",
]

print(fruits)

# append : adds new value at the end of the list

fruits.append("Pineapple")

print(fruits)

# pop: removes last value from list if index is not provided as parameter otherwise value at that index is removed from list

fruits.pop()  # removes last value

print(fruits)

fruits.pop(3)  # removes value at index 3

print(fruits)

numbers_list = [1, 8, 2, 7, 2, 21, 2, 15]

print(numbers_list)

# sort: sorts the list to ascending order

numbers_list.sort()

print(numbers_list)

# reverse: reverses the values of the list

numbers_list.reverse()

print(numbers_list)

# insert: insert provided value at given index

numbers_list.insert(2, 40)

print(numbers_list)

# remove: remove value from list by passing value as parameter

numbers_list.remove(15)

print(numbers_list)

print(numbers_list.count(2))  # counts the number of times value is repeated in the list
numbers_list.clear()  # clears all the values in the list

print(numbers_list)

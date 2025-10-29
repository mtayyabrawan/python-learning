"""
Methods related to sets
"""

usernames = {"mtayyabrawan", "askimtinan", "infowithawan", "tehqeqistan"}

print(usernames)

usernames.add("inabah")  # adds item to the set

print(usernames)

print(usernames.pop())  # randomly removes any item and retrun it

print(usernames)

usernames.remove(
    "mtayyabrawan"
)  # remove provided item from set gives error of item not found

print(usernames)

usernames.discard(
    "inabah"
)  # remove provided item from set does't throw error unlike .remove()

print(usernames)

usernames.clear()  # remove all items from set

print(usernames)

number_set1 = {5, 89, 34, 8, 9, 4, 5, 78, 34}
number_set2 = {23, 59, 34, 90, 9, 4, 67, 78, 34}

union_set = number_set1.union(number_set2)
inter_set = number_set1.intersection(number_set2)

print(union_set)  # includes value of both sets
print(inter_set)  # includes value common in both sets

print(number_set1.issuperset({9, 2}))

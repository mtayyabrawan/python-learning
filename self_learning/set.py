# defining sets
emptySet = set()
marksSet = {10, 20, 89, 30, 40, 50, 80, 60, 70, 80, 90, 40, 100}
print(emptySet)
print(type(emptySet))
print(marksSet)
marksSet.add("Name")
print(marksSet)
# methods
marksSet.remove(100)
print(marksSet)
print(marksSet.pop())
print(marksSet)
# print(marksSet.clear())
# print(marksSet)
newSet = {982, 7, 90, 367, 0, 98, 45}
print(marksSet.union(newSet))
print(marksSet.intersection(newSet))

# list

marks = [68.8, 34, 90, 58, 66, 98]

print(marks)
print(type(marks))
print(len(marks))

# indexing and slicing

student = ["Muhammad Tayyab", 717, "Khaur", 20]

print(student[2])
print(student[-2])
student[0] = "Muhammad Tayyab Raza"
print(student)

print(student[2:])
print(student[-3:])

# list methods

student.append("Full Stack Developer")
print(student)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
student.reverse()
print(student)
student.remove(717)
print(student)
student.pop(-2)
print(student)
student.pop()
print(student)
student.insert(1, 717)
print(student)
print(student.index(20))
student.clear()
print(student)
print(student.count(20))
student.extend(marks)
print(student)

# tuples

tup = ()  # empty tuple
tup = (1,)  # with single value
tup = (67, 98, 45, 89, 34)
print(tup)
print(type(tup))

# indexing and slicing
print(tup[1])
# tup(0) = 100 # not valid for tuples unlike lists tuples are immutable
print(tup[-3])
print(tup[2:5])

# tuple methods

print(tup.count(98))
print(tup.index(45))

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

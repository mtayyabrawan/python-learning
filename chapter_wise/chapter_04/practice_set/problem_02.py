"""
Write a program to accept marks of 6 students and display them in a sorted
manner.
"""

marks_of_students = []

marks_of_students.append(int(input("Student 1 Enter your marks : ")))
marks_of_students.append(int(input("Student 2 Enter your marks : ")))
marks_of_students.append(int(input("Student 3 Enter your marks : ")))
marks_of_students.append(int(input("Student 4 Enter your marks : ")))
marks_of_students.append(int(input("Student 5 Enter your marks : ")))
marks_of_students.append(int(input("Student 6 Enter your marks : ")))
marks_of_students.append(int(input("Student 7 Enter your marks : ")))

marks_of_students.sort()
marks_of_students.reverse()

print(
    f"""Marks of Students Sorted in Descending order :
            Student 1 Marks : {marks_of_students[0]}
            Student 2 Marks : {marks_of_students[1]}
            Student 3 Marks : {marks_of_students[2]}
            Student 4 Marks : {marks_of_students[3]}
            Student 5 Marks : {marks_of_students[4]}
            Student 6 Marks : {marks_of_students[5]}
            Student 7 Marks : {marks_of_students[6]}"""
)

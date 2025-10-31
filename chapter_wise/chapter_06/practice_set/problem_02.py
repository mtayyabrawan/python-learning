"""
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
"""

total_marks = 300

marks = []

marks.append(int(input("Enter first subject marks : ")))
marks.append(int(input("Enter second subject marks : ")))
marks.append(int(input("Enter third subject marks : ")))

total_percentage = ((marks[0] + marks[1] + marks[2]) * 100) / 300

if total_percentage >= 40 and marks[0] >= 33 and marks[1] >= 33 and marks[2] >= 33:
    print(f"Congratulations! You have passed the exams with {total_percentage}%")
else:
    print(f"You got failed with {total_percentage}")

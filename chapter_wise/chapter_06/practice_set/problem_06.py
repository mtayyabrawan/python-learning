"""
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
"""

marks = int(input("Enter your marks : "))
grade = None

if marks >= 90 and marks <= 100:
    grade = "Ex"
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 60 and marks < 70:
    grade = "C"
elif marks >= 50 and marks < 60:
    grade = "D"
else:
    grade = "F"

print(f"Your Grade is : {grade}")

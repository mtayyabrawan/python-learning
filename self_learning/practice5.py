# store word meanings in dict

meanings = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print(meanings)
# assuming classrooms for students
list_of_std_subs = ["python", "java", "cpp", "python",
                    "javascript", "java", "python", "java", "c"]

classroomsRequired = len(set(list_of_std_subs))
print(classroomsRequired)

# store std marks with subjs names

marks = {}
marks.update({input("Enter name of first subject : "):
             float(input("Now enter marks of that subjs : "))})
marks.update({input("Enter name of second subject : "):
             float(input("Now enter marks of that subjs : "))})
marks.update({input("Enter name of third subject : "):
             float(input("Now enter marks of that subjs : "))})
print(marks)

# store 9 and 9.0 in set

newSet = {90, 78, 256, 67, 23, 9, "9.0"}
print(newSet)

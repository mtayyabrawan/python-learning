# lists
# store names of movies

fav_movies = [input("Enter name of your 1st fav movie:"), input(
    "Enter name of your 2nd fav movie:"), input("Enter name of your 3rd fav movie:")]
print(fav_movies)

# palindrome list check

palin_list = [3, 7, 8, 4, 3]

list_copy = palin_list.copy()
list_copy.reverse()
if palin_list == list_copy:
    print("List is palindrome")
else:
    print("List is not palindrome")

# tuples
# count no of students with grade A in a particular tuple
grades = ("C", "D", "A", "A", "B", "B", "A")

print(f"{grades.count("A")} students got 'A' Grade")

# store above tuple values in list and sort it

grades_list = []
grades_list.extend(grades)
grades_list.sort()
print(grades_list)

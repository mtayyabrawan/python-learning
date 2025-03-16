# if-elif-else
age = int(input("Enter your age : "))

if (age >= 18 and age <= 70):
    print("You are eligible to drive")
elif (age >= 70):
    print("You are to old to drive")
else:
    print("You can't drive")

# match-case
light = input("Enter the color of light : ")

match light:
    case "red":
        print("Don't move, Stop now")
    case "green":
        print("You can go now")
    case "yellow":
        print("Get ready to go")
    case _:
        print("Invalid light color")

# nested conditions
# checking marriage

age = int(input("Enter your age : "))
gender = input("Enter your gender")

if age >= 18:
    if gender == "female" or gender == "male":
        print("You are now eligible to marry")
    else:
        print("You can't marry")
elif age >= 16:
    if gender == "female":
        print('As you are a girl you can marry according to law of pakistan')
    elif gender == "male":
        print("You are not yet eligible to marry")
    else:
        print("You can't marry")
else:
    print("You are too young so you can't marry now")

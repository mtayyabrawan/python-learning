# Variables
# Valid variable names
name = "Tayyab"
item_count = 5
item1 = "Book"
# Invalid variable names
# 1name , $name
# Data Types
# Integer
age = 20
print("Age :", age, "Data type of age variable is :", type(age))
# Float
average = 5.7
print("Average marks :", average, "Type of average variable is :", type(average))
# String
username = "tayyabraza1918"
print("Username :", username, "Type of username variable is :", type(username))
# Bool
isVerified = True
print("User Verification Status :", isVerified,
      "Type of isVerified variable is :", type(isVerified))
# None
nothingToStore = None
print("Type of nothingToStore variable is :", type(nothingToStore))
# Operators
# Arithmetic Operators (+,-,*,/,//,%,**)
a = 12
b = 5
Sum = a + b
diff = a - b
prod = a * b
div = a / b
floDiv = a // b
mod = a % b
power = a ** b
print("Sum :", Sum)
print("Difference :", diff)
print("Product :", prod)
print("Division :", div)
print("Floor Division :", floDiv)
print("Modulus :", mod)
print("a^b :", power)
# Relational Operators (<,>,<=,>=,==,!=)
print("a > b", a > b)
print("a < b", a < b)
print("a >= b", a >= b)
print("a <= b", a <= b)
print("a == b", a == b)
print("a != b", a != b)
# Assignment Operators (=,+=,-=,*=,/=,//=,**=,%=)
a = 60
a += 5  # a = a + 5
a -= 5  # a = a - 5
a *= 5  # a = a * 5
a /= 5  # a = a / 5
a //= 5  # a = a // 5
a **= 5  # a = a ** 5
a %= 5  # a = a % 5
print(a)
# Logical Operators (and,or,not)
print(a > b and b == a)
print(a < b or b == a)
print(not (a > b))
# f string
print(f"My age is {age}")
# Multiline string
sentence = """loremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremloremlorem
"""
print(sentence)
# type casting
print(type(age))
age = str(age)
print(type(age))
age = float(age)
print(type(age))
age = bool(age)
print(age, type(age))
# user input
name = input("Enter your name here : ")
print(f"Welcome back! {name}")
age = int(input("Enter your age here : "))
print(f"You entered {age}")

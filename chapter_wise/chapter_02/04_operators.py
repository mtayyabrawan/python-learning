"""
Operators in Python

1. Arithmetic Operators
2. Assignment Operators
3. Comparision Operators
4. Logical Operators
"""

# 1. Arithmetic Operators: used to perform arithmetic operations (+,-,*,/)

a , b = 28 , 45

sum = a + b
diff = a - b
product = a * b
division = b / a
mod = a % b #modulus
power = a ** b # power

print(sum)
print(diff)
print(product)
print(division)
print(mod)
print(power)

# Assignment Operators: used to assign values to variabels (+=,-=,,*=,/=,%=,=)

age = 20
age -= 1
age += 1
age *= 1
age /= 1
# age %= 1
age **= 1

print(age)

# Comparision Operators: used to compare values (<=,<,>=,>,==,!=)

print(age > 25)
print(age >= 20)
print(age < 20)
print(age <= 20)
print(age == 23)
print(age != 23)

# Logical Operators: (and, or, not)

# Truth Table for and

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Truth Table for or

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Truth Table for not

print(not True)
print(not False)
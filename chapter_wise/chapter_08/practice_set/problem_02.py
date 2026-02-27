"""
Write a python program using function to convert Celsius to Fahrenheit.
"""

# Formula : F =  ((C * 9) / 5 ) + 32


def celsius_fahrenheit(temp_in_c):
    return ((temp_in_c * 9) / 5) + 32


def fahrenheit_celsius(temp_in_f):
    return ((temp_in_f - 32) * 5) / 9


print(f"50 Celsius = {celsius_fahrenheit(50)} Fahrenheit")
print(f"100 Fahrenheit = {round(fahrenheit_celsius(100),2)} Celsius")

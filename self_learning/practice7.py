# print elems of list
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in numbers:
    print(num)
# find number in the tuple using for loop
numbers = tuple(numbers)
find_number = int(input("Enter number that you want to find : "))

for num in enumerate(numbers):
    if (num[1] == find_number):
        print(f"Found number {find_number} at index {num[0]}")
    elif num[0] == (len(numbers) - 1):
        print(f"'{find_number}' not found")

# print 1 to 100 using range and for

for n in range(1, 101):
    print(n)

# print 100 to 1 using range and for

for n in range(100, 0, -1):
    print(n)

# print multiplication table of number n using for

table = int(input("Enter table number : "))
for n in range(1, 11):
    print(f"{table} * {n} = {table * n}")

# factorial of first n numbers

factorial_num = int(input("Enter number here : "))

factorial = 1
for n in range(1, factorial_num+1):
    factorial *= n
print(f"Factorial of {factorial_num} is {factorial}")

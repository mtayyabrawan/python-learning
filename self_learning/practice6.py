# print 1 to 100 using while
idx = 1
while idx <= 100:
    print(idx)
    idx += 1
# print 100 to 1 using while
idx = 100
while idx >= 1:
    print(idx)
    idx -= 1
# table of n number
n = int(input("Enter any number : "))

idx = 1
while idx <= 10:
    print(f"{n} * {idx} = {n*idx}")
    idx += 1

# print numbers of a specific list
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
# search x in tuple using while loop
nums = tuple(nums)

x = int(input("Enter number you want to search : "))
idx = 0
while idx < len(nums):
    if (nums[idx] == x):
        print(f"Your number '{x}' found at index {idx}")
        break
    idx += 1
else:
    print("Number not found")

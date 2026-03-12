# Map

from functools import reduce


l = [3,4,5,6,7,8,9,2]

square = lambda x:x*x

print(list(map(square,l)))

# Filter

def even(num:int) -> bool:
    if(num % 2 == 0):
        return True
    else:
        return False

print(list(filter(even,l)))

# Reduce

def greater(a:int,b:int) -> int:
    if(a>b):
        return a
    else:
        return b

print(reduce(greater,l))
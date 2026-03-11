"""
Write a program to print third, fifth and seventh element from a list using enumerate
function.
"""

l = [23,74,67,34,90,56,35,93.28,47,39]

for idx,item in enumerate(l):
    if(idx+1 == 5 or idx+1 == 6 or idx+1 == 7 ):
        print(f"{idx+1}th item is {item}")
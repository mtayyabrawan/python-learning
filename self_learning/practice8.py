# WAF to print length of list


def lengthPrint(givenList):
    print(len(givenList))


lengthPrint([1, 5, 8, 20, 67])

lengthPrint(["tayyab", 5, 8, 20, 67, "raza"])
# WAF to print elem of list in single line


def printList(givenList):
    for elem in givenList:
        print(elem, end=" ")


printList([6, "hello", 717, 967, 1071, 1453])

# WAF to print factorial of n


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(0))

# WAF to convert PKR to USD


def PKRToUSD(pkr):
    _1usd = 256
    return pkr / _1usd


print(PKRToUSD(50000))


# WAF to calculate sum of first n natural numbers using recursion


def sumOfN(n):
    if n < 1:
        return 0
    return sumOfN(n - 1) + n


print(sumOfN(100))


# WAF to print elem of list (recursive)


def recPrint(givenList, idx=0):
    if len(givenList) == idx:
        return
    print(givenList[idx])
    return recPrint(givenList, idx + 1)


recPrint([2, 7, 900, 717, 967, 2103508, "tayyab", "awan", "pasha"])

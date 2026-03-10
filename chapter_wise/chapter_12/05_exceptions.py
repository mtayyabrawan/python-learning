try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except ValueError as e:
    print("value", e)
except Exception as e:
    print(e)

try:
    num1 = 4
    num2 = 2
    print(sum := num1/num2)
except Exception as e:
    print(e)
else:
    print("Executes only if the try block run without any error")

age = int(input("Enter you age to vote: "))
if (age < 18):
    raise Exception("Age must be >= 18")
else:
    print("You successfully casted vote")


def check_vowel(char: str) -> bool:
    try:
        if (type(char) != type(str())):
            raise TypeError("Invalid type expecting str character")
        match char.lower():
            case "a":
                return True
            case "i":
                return True
            case "o":
                return True
            case "u":
                return True
            case "e":
                return True
            case _:
                return False
    except Exception as e:
        print(e)
        return False
    finally:
        print("Always run even after return statement")


check_vowel("A")

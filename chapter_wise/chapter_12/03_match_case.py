character = input(
    "Enter a character to check whether it is vowel or not : ")

match character.lower():
    case "a":
        print(f"'{character}' is vowel")
    case "e":
        print(f"'{character}' is vowel")
    case "i":
        print(f"'{character}' is vowel")
    case "o":
        print(f"'{character}' is vowel")
    case "u":
        print(f"'{character}' is vowel")
    case _:
        print(f"'{character}' is not a vowel")

"""
PROJECT 1: SNAKE, WATER, GUN GAME
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.
"""

import random


def print_result(result):
    if result == "draw":
        print("It is a draw")
    else:
        print(f"You {result}!")


def play_again():
    user_resp = (
        input("Press 'Y/y' to play again or any other key to exit the game: ")
        .strip()
        .lower()
    )
    if user_resp == "y":
        return main()
    else:
        return


def main():
    choice_list = ["s", "w", "g"]
    choice_mapping = {"s": "Snake", "w": "Water", "g": "Gun"}
    computer_input = random.choice(choice_list)
    user_input = (
        input("Enter your choice (s (snake), w (water), g (gun)): ").strip().lower()
    )
    if user_input not in choice_list:
        print("You entered wrong choice")
    else:
        print(
            f"You entered {choice_mapping[user_input]}\nComputer entered {choice_mapping[computer_input]}"
        )
        if user_input == computer_input:
            print_result("draw")
        elif user_input == "s" and computer_input == "w":
            print_result("win")
        elif user_input == "g" and computer_input == "w":
            print_result("loose")
        elif user_input == "s" and computer_input == "g":
            print_result("loose")
        elif user_input == "w" and computer_input == "g":
            print_result("win")
        elif user_input == "w" and computer_input == "s":
            print_result("loose")
        elif user_input == "g" and computer_input == "s":
            print_result("win")
        else:
            print("Something went wrong")
    return play_again()


main()

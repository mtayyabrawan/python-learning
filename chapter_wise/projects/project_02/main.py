"""
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module.
"""


from random import randint


def play_again():
    user_resp = (
        input("Press 'Y' to play again or any other key to exit the game: ")
        .strip()
        .lower()
    )
    if user_resp == "y":
        return main()
    else:
        return


def play(num, attempt):
    user_input = int(input("Enter number to guess: "))
    attempt += 1
    if (user_input == num):
        print(
            f"Congratulations! You guessed the number '{num}' in {attempt} attempts.")
        return
    elif (user_input < num):
        print("Higher number please!")
        return play(num, attempt)
    elif (user_input > num):
        print("Lower number please!")
        return play(num, attempt)


def main():
    rand_num = randint(1, 100)
    play(rand_num, 0)
    play_again()


main()

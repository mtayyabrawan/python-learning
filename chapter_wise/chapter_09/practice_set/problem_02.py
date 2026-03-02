"""
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
"""

import random


def game():
    return random.randint(1, 100)


def keep_score(score):
    with open("hiscore.txt") as hi_score_file:
        hiscore = hi_score_file.read().strip()
        if (not hiscore or not hiscore.isnumeric()):
            hiscore = "0"
        if int(hiscore) < score:
            hiscore = str(score)
    with open("hiscore.txt", "w") as file:
        file.write(hiscore)
        return


keep_score(game())

"""
📚 Topic: Chapter 09 Exercise - Problem 2

This script demonstrates chapter 09 exercise - problem 2 using conditions,
functions, classes and file or path operations.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 2
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 2 affects the result.
"""


# The game() function in a program lets a user play a game and returns the
# score
# as an integer. You need to read a file 'Hi-score.txt’
# which is either blank or
# contains the previous Hi-score. You need to write a program to update the
# Hiscore whenever the game() function breaks the Hi-score.


import random


def game():
    print("Your paying the game  ")
    score = random.randint(1, 90)
    print(f"Your score is {score}")

    with open('highscore.txt') as f:
        highscore = f.read()
        if highscore != '':
            highscore = int(highscore)
        else:
            highscore = 0
    if score > highscore:
        with open('highscore.txt', 'w')as f:
            f.write(str(score))


game()

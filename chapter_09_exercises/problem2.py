# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file 'Hi-score.txt’ 
# which is either blank or
# contains the previous Hi-score. You need to write a program to update the
# Hiscore whenever the game() function breaks the Hi-score.


import random
def game():
    print("Your paying the game  ")
    score=random.randint(1,90)
    print(f"Your score is {score}")

    with open('highscore.txt') as f:
        highscore=f.read()  
        if  highscore!='':
            highscore=int(highscore)
        else:
            highscore=0
    if score>highscore:
        with open('highscore.txt','w')as  f:
            f.write(str(score))
game()
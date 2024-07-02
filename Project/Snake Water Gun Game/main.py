'''
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.
1-s
2-w
3-g

1 - 3 you win
1 - 2 you loose

2-1 you win
2-3 you loose

3-2 you win
3-1 you loose
'''
import random
comp=random.randint(1,3)
# print(comp)
user=int(input("Enter 1(snake) - 2(water) - 3(gun) "))
if comp==user:
    print("Die !!!!!!")
else:
    if(comp==1 and user==3):
        print("You win")
    
    elif(comp==1 and user==2):
        print("You loose")
    
    elif(comp==2 and user==1):
        print("You win")
    
    elif(comp==3 and user==1):
        print("You loose")
    
    elif(comp==3 and user==2):
        print("You win")
    
    elif(comp==2 and user==3):
        print("You loose")
    
    else:
        print("Invalid Input")

print(f"You can choose {user} and computer can choose {comp}")
def game():
        print(logo)
        com=random.randint(1,100)
        print("............. Welcome to Number gessing game .............")
        print("I am thinking of a game between 1 to 100.")
        print(f"Pssst, the correct answer is {com}")
        difficulty=input("Choose your difficulty. Type 'easy' or 'hard'").lower()
        attempt=10

        if difficulty=='hard':
                attempt-=5
                print(f"You have {attempt} attempts remaining to guess the number")
                print(f"You can gesse the number in  {attempt} attempt")

        elif difficulty=='easy':
                print(f"You have {attempt} attempts remaining to guess the number")
        else:
                exit()
        while True:
                print(f"You can gesse the number in  {attempt} attempt")
                user=int(input("Gesses the number : "))
                if user<com:
                        print("You enter more value ...")
                elif user>com:
                        print("You enter less value ...")
                elif com==user:
                        print("You win !!")
                        break
                if attempt==1:
                        break
                attempt-=1

import random
from img import logo
game()

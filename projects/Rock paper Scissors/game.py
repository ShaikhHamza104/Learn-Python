import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user >= 3 or user < 0:
    print("Invalid number, you lose!")
else:
    print(f"You chose:\n{game_images[user]}")

    comp = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[comp]}")

    if user == comp:
        print("It's a draw!")
    elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
        print("You win!")
    else:
        print("You lose!")

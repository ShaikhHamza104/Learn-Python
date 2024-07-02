import random
comp=random.randint(0,2)
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
user=int(input("What do you choose? type 0 for Rock 1 for Paper 2 for Scissors."))
if user==0:
    print(f"{rock}")
elif user==1:
    print(f"{paper}")
elif user==2:
    print(f"{scissors}")

if comp==0:
    print(f"Computer choose\n{rock}")
elif comp==1:
    print(f"Computer choose\n{paper}")
elif comp==2:
    print(f"Computer choose\n{scissors}")


if user==comp:
    print("Die !! ")
else:
    if user==0 or comp==1:
        print("You loose")
    elif user==0 or comp==2:
        print("You win")
    
    elif user==1 or comp==2:
        print("You win")
    elif user==1 or comp==2:
        print("You loose")

    
    elif user==2 or comp==0:
        print("You loose")
    elif user==2 or comp==1:
        print("You win")

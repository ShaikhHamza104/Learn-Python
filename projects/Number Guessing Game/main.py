import random 

comp : int = random.randint(1,100)
guess : int = 0
max_attempt = 10
game_is_on: bool= True
print("------------------Welcome to number guessing game------------------")
while max_attempt>=0:
    print(f"You guess the number in {max_attempt} times")
    user_guess : int = int(input("Guess the number from 1 - 100: ")) 
    guess+=1
    max_attempt-=1
    if user_guess == comp:
        print(f"You can guess the number in {guess}.")
        break
    elif user_guess < comp:
        print("Last guess was too high!")
        
    elif user_guess > comp:
        print("Last guess was too low!")
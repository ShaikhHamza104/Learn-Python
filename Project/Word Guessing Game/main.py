import random

# Define constants
WORDS: tuple = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
no_of_guesses: int = 0
attempts_left: int = 10
game_is_on: bool = True

if __name__ == "__main__":
    print("************** Welcome To Word Guessing Game **************")
    random_word = random.choice(WORDS)
    
    while game_is_on:
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left.")
            user_word = input("Guess the word:\n")
            no_of_guesses += 1
            attempts_left -= 1
            
            if user_word == random_word:
                print(f"Congratulations! You guessed the word '{random_word}' in {no_of_guesses} guesses.")
                game_is_on = False
        else:
            print(f"Sorry! You've run out of attempts. The correct word was '{random_word}'.")
            game_is_on = False
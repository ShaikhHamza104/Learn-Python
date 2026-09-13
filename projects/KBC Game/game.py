import random


def get_questions():
    """
    Returns a list of questions for the KBC game.
    Each question is a dictionary with a question, options,
    and the correct answer.
    """
    return [
        {
            "question": "What is the capital of France?",
            "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "correct_answer": "c",
        },
        {
            "question": "Who wrote 'Pride and Prejudice'?",
            "options": [
                "a) Charlotte Bronte",
                "b) Emily Brontë",
                "c) Jane Austen",
                "d) Mary Shelley",
            ],
            "correct_answer": "c",
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["a) Au", "b) Ag", "c) Go", "d) Gd"],
            "correct_answer": "a",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
            "correct_answer": "b",
        },
        {
            "question": (
                "Who was the first President of the United States?"
            ),
            "options": [
                "a) Abraham Lincoln",
                "b) George Washington",
                "c) Thomas Jefferson",
                "d) John Adams",
            ],
            "correct_answer": "b",
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["a) 1912", "b) 1915", "c) 1918", "d) 1920"],
            "correct_answer": "a",
        },
        {
            "question": (
                "Mount Everest is located in which mountain range?"
            ),
            "options": ["a) Andes", "b) Alps", "c) Rockies", "d) Himalayas"],
            "correct_answer": "d",
        },
        {
            "question": "Which is the longest river in the world?",
            "options": [
                "a) Amazon",
                "b) Nile",
                "c) Yangtze",
                "d) Mississippi",
            ],
            "correct_answer": "b",
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": [
                "a) James Cameron",
                "b) Steven Spielberg",
                "c) Christopher Nolan",
                "d) Martin Scorsese",
            ],
            "correct_answer": "c",
        },
        {
            "question": (
                "Which actor played the character of Harry Potter "
                "in the movie series?"
            ),
            "options": [
                "a) Rupert Grint",
                "b) Elijah Wood",
                "c) Daniel Radcliffe",
                "d) Tom Felton",
            ],
            "correct_answer": "c",
        },
        {
            "question": "Which country won the FIFA World Cup in 2018?",
            "options": [
                "a) Brazil",
                "b) Germany",
                "c) Argentina",
                "d) France",
            ],
            "correct_answer": "d",
        },
        {
            "question": (
                "In which sport would you perform a slam dunk?"
            ),
            "options": [
                "a) Baseball",
                "b) Basketball",
                "c) Volleyball",
                "d) Tennis",
            ],
            "correct_answer": "b",
        },
    ]


def play_game(questions):
    """
    Plays a round of the KBC game.
    """
    question = random.choice(questions)

    print("\n" + question['question'])
    for option in question['options']:
        print(option)

    user_answer = input("Enter your option: ").lower()

    if user_answer == question['correct_answer']:
        print("You are right!")
    else:
        print("You are wrong.")
        print(f"The correct answer is: {question['correct_answer'].upper()}")


def main():
    """
    Main function to run the KBC game.
    """
    questions = get_questions()

    print("*********************************************************************************************************")  # noqa: E501
    print("*********************************** WELCOME TO KBC GAME *************************************************")  # noqa: E501
    print("*********************************************************************************************************")  # noqa: E501

    while True:
        play_game(questions)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()

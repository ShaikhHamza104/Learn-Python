import random
import pymongo
# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["MCQ"]
collection = db["Question"]
# Data with custom _id starting from 101, including correct answers
data = [
    {"_id": 101, "question": "What is the capital of France?", "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"], "correct_answer": "c"},
    {"_id": 102, "question": "Who wrote \"Pride and Prejudice\"?", "options": ["a) Charlotte Bronte", "b) Emily Brontë", "c) Jane Austen", "d) Mary Shelley"], "correct_answer": "c"},
    {"_id": 103, "question": "What is the chemical symbol for gold?", "options": ["a) Au", "b) Ag", "c) Go", "d) Gd"], "correct_answer": "a"},
    {"_id": 104, "question": "Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"], "correct_answer": "b"},
    {"_id": 105, "question": "Who was the first President of the United States?", "options": ["a) Abraham Lincoln", "b) George Washington", "c) Thomas Jefferson", "d) John Adams"], "correct_answer": "b"},
    {"_id": 106, "question": "In which year did the Titanic sink?", "options": ["a) 1912", "b) 1915", "c) 1918", "d) 1920"], "correct_answer": "a"},
    {"_id": 107, "question": "Mount Everest is located in which mountain range?", "options": ["a) Andes", "b) Alps", "c) Rockies", "d) Himalayas"], "correct_answer": "d"},
    {"_id": 108, "question": "Which is the longest river in the world?", "options": ["a) Amazon", "b) Nile", "c) Yangtze", "d) Mississippi"], "correct_answer": "b"},
    {"_id": 109, "question": "Who directed the movie \"Inception\"?", "options": ["a) James Cameron", "b) Steven Spielberg", "c) Christopher Nolan", "d) Martin Scorsese"], "correct_answer": "c"},
    {"_id": 110, "question": "Which actor played the character of Harry Potter in the movie series?", "options": ["a) Rupert Grint", "b) Elijah Wood", "c) Daniel Radcliffe", "d) Tom Felton"], "correct_answer": "c"},
    {"_id": 111, "question": "Which country won the FIFA World Cup in 2018?", "options": ["a) Brazil", "b) Germany", "c) Argentina", "d) France"], "correct_answer": "d"},
    {"_id": 112, "question": "In which sport would you perform a slam dunk?", "options": ["a) Baseball", "b) Basketball", "c) Volleyball", "d) Tennis"], "correct_answer": "b"}
]

# Insert data into the collection
# collection.insert_many(data)
while True:
    # Generate a random question ID between 101 and 112
    random_question_id = random.randint(101, 112)

    # Fetch the question with the random ID, including the correct answer
    question = collection.find_one({"_id": random_question_id}, {"_id": 0})
    print('''
        *********************************************************************************************************
        *********************************** WELCOME TO KBC GAME ***********************************\n
        *********************************************************************************************************
        ''')
    # Check if a question was found
    if question:
        # Print the question text
        print(question['question'])
        # Print each option
        for option in question['options']:
            print(option)
        candidate = input("Enter your option: ")
        if candidate == question['correct_answer']:
            print("You are right!")
        else:

            print("You are wrong ")
            # Print the correct answer
            print(f"Correct answer: {question['correct_answer']}")
    else:
        print("No question found with the given ID.")
    play_again=input("Do you want to play again")
    if  not play_again=='y' or  play_again=='yes':
        break
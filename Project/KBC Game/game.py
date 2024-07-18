import random

option = {
    1: '''a) Berlin
b) Madrid
c) Paris
d) Rome''',
    2: '''a) Charlotte Brontë
b) Emily Brontë
c) Jane Austen
d) Mary Shelley''',
    3: '''a) Au
b) Ag
c) Go
d) Gd''',
    4: '''a) Venus
b) Mars
c) Jupiter
d) Saturn''',
    5: '''a) Abraham Lincoln
b) George Washington
c) Thomas Jefferson
d) John Adams''',
    6: '''a) 1912
b) 1915
c) 1918
d) 1920''',
    7: '''a) Andes
b) Alps
c) Rockies
d) Himalayas''',
    8: '''a) Amazon
b) Nile
c) Yangtze
d) Mississippi''',
    9: '''a) James Cameron
b) Steven Spielberg
c) Christopher Nolan
d) Martin Scorsese''',
    10: '''a) Rupert Grint
b) Elijah Wood
c) Daniel Radcliffe
d) Tom Felton''',
    11: '''a) Brazil
b) Germany
c) Argentina
d) France''',
    12: '''a) Baseball
b) Basketball
c) Volleyball
d) Tennis'''
}

# List of questions
list_of_question = [
    "What is the capital of France?",
    "Who wrote \"Pride and Prejudice\"?",
    "What is the chemical symbol for gold?",
    "Which planet is known as the Red Planet?",
    "Who was the first President of the United States?",
    "In which year did the Titanic sink?",
    "Mount Everest is located in which mountain range?",
    "Which is the longest river in the world?",
    "Who directed the movie \"Inception\"?",
    "Which actor played the character of Harry Potter in the movie series?",
    "Which country won the FIFA World Cup in 2018?",
    "In which sport would you perform a slam dunk?"
]

# List of correct answers corresponding to the questions
correct_answers = [
    'c',  # Paris
    'c',  # Jane Austen
    'a',  # Au
    'b',  # Mars
    'b',  # George Washington
    'a',  # 1912
    'd',  # Himalayas
    'b',  # Nile
    'c',  # Christopher Nolan
    'c',  # Daniel Radcliffe
    'd',  # France
    'b'   # Basketball
]

question_index = random.randint(0, len(list_of_question) - 1)
print('''
*********************************************************************************************************
*********************************** WELCOME TO KBC GAME ***********************************\n
*********************************************************************************************************
''')
print(list_of_question[question_index])
print(option.get(question_index + 1))
candidate = input("Enter your option: ")

if candidate.lower() == correct_answers[question_index]:
    print("You are right ")
else:
    print("You worng")
    print(correct_answers[question_index],"is correct")

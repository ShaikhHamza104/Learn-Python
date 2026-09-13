"""
📚 Topic: Chapter 05 Exercise - Problem 6

This script demonstrates chapter 05 exercise - problem 6 using user input
and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 05 exercise - problem 6
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 05 exercise - problem 6 affects the result.
"""


# 📚 Create an empty dictionary
# We will store the friend's name as the key
# and their favorite language as the value.
language = {}


# 👤 Get the first friend's name and favorite language
friend = input("Enter Friend name: ")
lang = input("Enter your favorite language: ")

# ➕ Add the name and language to the dictionary
language.update({friend: lang})


# 👤 Get the second friend's name and favorite language
friend = input("Enter Friend name: ")
lang = input("Enter your favorite language: ")

# ➕ Add the second friend's details to the dictionary
language.update({friend: lang})


# 👤 Get the third friend's name and favorite language
friend = input("Enter Friend name: ")
lang = input("Enter your favorite language: ")

# ➕ Add the third friend's details to the dictionary
language.update({friend: lang})


# 👤 Get the fourth friend's name and favorite language
friend = input("Enter Friend name: ")
lang = input("Enter your favorite language: ")

# ➕ Add the fourth friend's details to the dictionary
language.update({friend: lang})


# 📋 Display all friends and their favorite languages
print(language)

# Example output:
# {
#     'Rohan': 'Python',
#     'Harry': 'Java',
#     'Sonali': 'C++',
#     'Yusuf': 'JavaScript'
# }

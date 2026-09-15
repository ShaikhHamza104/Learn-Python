"""
📚 Topic: Chapter 05 Exercise - Problem 6

Collect favorite programming languages from friends and store them in a
dictionary.

💡 Key points:
    1️⃣ Using friend names as dictionary keys
    2️⃣ Storing language choices as values
    3️⃣ Iterating over user input to populate dictionary entries
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

"""
📚 Topic: Chapter 05 Exercise - Problem 1

This script demonstrates chapter 05 exercise - problem 1 using user input,
conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 05 exercise - problem 1
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 05 exercise - problem 1 affects the result.
"""


# 📚 Create a dictionary of Hindi words and their English meanings
words = {
    "Kitab": "Book",
    "Riyazi": "Math",
    "Dabba": "Box",
    "Rabber": "Erazor",
    "Maded": "Help",
    "Billi": "Cat",
}


# ⌨️ Ask the user to enter a word
# capitalize() makes the first character uppercase
# and converts the remaining characters to lowercase.
#
# Example:
# kitAB → Kitab
# billi → Billi
word = input("Enter a word : ").capitalize()


# 🔍 Look up the word in the dictionary
# get() returns the English meaning if the word exists.
# If the word is not found, it returns None.
print(words.get(word))

# Example:
# Enter a word : kitab
# Output:
# Book

"""
📚 Topic: Chapter 05 Exercise - Problem 1

Create a Hindi-to-English translation dictionary and allow users to look up
words.

💡 Key points:
    1️⃣ Storing translations in a dictionary mapping
    2️⃣ Handling user input for dynamic lookup
    3️⃣ Using `.get()` for safe lookup when a word is not found
"""
# 📚 Create a dictionary of Hindi words and their English meanings
words = {
    "Kitab": "Book",
    "Riyazi": "Math",
    "Dabba": "Box",
    "Rabber": "Eraser",
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

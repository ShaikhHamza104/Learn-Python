"""
📚 Topic: Problem4

This script demonstrates problem4 using regex, functions and exception
handling.

💡 Key points:
    1️⃣ the basic syntax for problem4
    2️⃣ how regex fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem4 affects the result.
"""

import re


# 4. Write a program that finds all the words that start with a
# capital letter in a sentence entered by the user.
def findCapitalWords():
    try:
        text = input("Enter a sentence: ")
        pattern = r"\b[A-Z][a-z]*\b"
        capital_words = re.findall(pattern, text)

        if capital_words:
            print("Capitalized words found:", capital_words)
        else:
            print("No capitalized words found")
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")


findCapitalWords()

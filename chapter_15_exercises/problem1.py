"""
📚 Topic: Problem1

This script demonstrates problem1 using regex, functions and exception
handling.

💡 Key points:
    1️⃣ the basic syntax for problem1
    2️⃣ how regex fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem1 affects the result.
"""

import re


# 1. Write a program that takes a sentence as input and extracts all
# email addresses found inside it using regex.
def extractEmails():
    try:
        text = input("Enter some text with emails in it: ")
        pattern = r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}"
        emails = re.findall(pattern, text)

        if emails:
            print("Emails found:", emails)
        else:
            print("No emails found in the text")
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")


extractEmails()

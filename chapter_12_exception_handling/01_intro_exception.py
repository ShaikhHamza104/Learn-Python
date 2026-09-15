"""
📚 Topic: Introduction to Exception Handling

This script introduces Python's `try-except` mechanism to catch runtime errors
gracefully without crashing programs.

💡 Key points:
    1️⃣ Anticipating potential runtime failures with `try`
    2️⃣ Handling specific error conditions inside `except`
    3️⃣ Maintaining program execution continuity after errors

🧠 Beginner tip:
    Exceptions are not bugs; they are unexpected runtime events (like missing
    files or bad user input) that programs should handle smoothly.
"""


# This code generates an error for text, names, characters, or float input.
# a=int(input("Enter a number : "))

try:
    a = int(input("Enter a number : "))
except ValueError:
    print("Error !! Please enter a valid number ")

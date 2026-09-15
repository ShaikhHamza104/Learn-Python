"""
📚 Topic: Functions with User Input

This script demonstrates interactive functions that accept user input and
produce personalized outputs.

💡 Key points:
    1️⃣ Prompting input from within a function body
    2️⃣ String formatting and concatenation in output
    3️⃣ Reusability across multiple invocations

🧠 Beginner tip:
    Whenever possible, pass values into functions as arguments rather than
    reading directly with `input()` inside the function.
"""


def good_day():
    name = input("Enter your name ")
    print("Good Day " + name)


good_day()

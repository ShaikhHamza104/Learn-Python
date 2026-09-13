"""
📚 Topic: Chapter 08 Exercise - Problem 2

This script demonstrates chapter 08 exercise - problem 2 using user input,
functions, classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 08 exercise - problem 2
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 08 exercise - problem 2 affects the result.
"""


# F=(9/5)C+32


def celsiusToFahrenheit(f):

    return 5 * (f - 32) / 9


f = int(input("Enter temperature in F : "))
print(f"Fahrenheit {f} to celsius  is {round(celsiusToFahrenheit(f), 2)}")

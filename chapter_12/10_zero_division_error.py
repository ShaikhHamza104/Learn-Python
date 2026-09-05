"""
📚 Topic: 10 Zero Division Error

This script demonstrates 10 zero division error using user input, conditions
and exception handling.

💡 Key points:
    1️⃣ the basic syntax for 10 zero division error
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    10 zero division error affects the result.
"""


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
except ValueError:
    print("Please enter a valid number ")

except ZeroDivisionError:
    print("You can try to dividing number by 0")

else:
    print(c)

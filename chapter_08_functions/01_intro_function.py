"""
📚 Topic: Introduction to Functions

This script demonstrates defining and invoking reusable functions to
encapsulate logic and eliminate repetitive code.

💡 Key points:
    1️⃣ Function definition syntax with the `def` keyword
    2️⃣ Calling functions by name followed by parentheses `()`
    3️⃣ Modularizing code into clean, testable blocks

🧠 Beginner tip:
    Defining a function only stores its logic; code inside runs only when the
    function is explicitly called.
"""


# Function definition
def avg():
    a = int(input("Enter number : "))
    b = int(input("Enter number : "))
    c = int(input("Enter number : "))

    average = (a + b + c) / 3
    print(average)


# Function called
avg()
print("Thank you")
avg()
print("Thank you")
avg()
print("Thank you")
avg()
avg()
avg()

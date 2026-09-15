"""
📚 Topic: Introduction to Modules

This script demonstrates creating and importing custom modules to organize
functions and reusable code across files.

💡 Key points:
    1️⃣ Any Python file (`.py`) can serve as an importable module
    2️⃣ Importing modules using the `import` statement
    3️⃣ Calling module functions using dot notation: `module.function()`

🧠 Beginner tip:
    Module names should follow snake_case and be short, descriptive, and
    all-lowercase.
"""


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return f"Addition of {a} and {b} is {a + b}"

    def sub(self, a, b):
        return f"Subtraction of {a} and {b} is {a - b}"

    def mul(self, a, b):
        return f"Multiplication of {a} and {b} is {a * b}"

    def div(self, a, b):
        return f"Division of {a} and {b} is {(a / b):.2f}"

"""
📚 Topic: M01 Intro Module

This script demonstrates m01 intro module using functions and classes.

💡 Key points:
    1️⃣ the basic syntax for m01 intro module
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    m01 intro module affects the result.
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

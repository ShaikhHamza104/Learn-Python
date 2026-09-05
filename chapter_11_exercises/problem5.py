"""
📚 Topic: Chapter 11 Exercise - Problem 5

This script demonstrates chapter 11 exercise - problem 5 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 11 exercise - problem 5
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 11 exercise - problem 5 affects the result.
"""


# operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f"{self.x+other.x}+{self.y+other.y}"

    def __mul__(self, other):
        return f"{self.x*other.x}+{self.y*other.y}"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 * v2)

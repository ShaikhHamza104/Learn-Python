"""
📚 Topic: Chapter 11 Exercise - Problem 6

This script demonstrates chapter 11 exercise - problem 6 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 11 exercise - problem 6
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 11 exercise - problem 6 affects the result.
"""


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j +{self.k}"

    def __add__(self, other):
        return f"{self.i+other.i}i + {self.j+other.j}j + {self.k+other.k}k"

    def __mul__(self, other):
        return f"{self.i*other.i}i x {self.j*other.j}j x {self.k*other.k}k"


v1 = Vector(3, 4, 5)
v2 = Vector(4, 4, 5)
print(v1 + v2)

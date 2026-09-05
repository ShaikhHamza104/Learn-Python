"""
📚 Topic: Chapter 11 Exercise - Problem 7

This script demonstrates chapter 11 exercise - problem 7 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 11 exercise - problem 7
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 11 exercise - problem 7 affects the result.
"""


class Vector:
    def __init__(self, l):  # noqa: E741
        self.l = l  # noqa: E741

    def __len__(self):
        return len(self.l)


v1 = Vector([1, 2, 3, 8])
print(len(v1))

"""
📚 Topic: Chapter 11 Exercise - Problem 1

This script demonstrates chapter 11 exercise - problem 1 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 11 exercise - problem 1
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 11 exercise - problem 1 affects the result.
"""


class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"Two D Vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"Two D Vector is {self.i}i + {self.j}j + {self.k}k")


t = TwoDVector(12, 14)
t.show()
th = ThreeDVector(1, 2, 13)
th.show()

"""
📚 Topic: Chapter 10 Exercise - Problem 4

This script demonstrates chapter 10 exercise - problem 4 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 10 exercise - problem 4
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 10 exercise - problem 4 affects the result.
"""


import math


class Calculator:
    def findSquare(self, n):
        print("{} * {} = {}".format(n, n, n**2))

    def findCube(self, n):
        print("{} * {} * {} = {}".format(n, n, n, n**3))

    def findRoot(self, n):
        print(math.sqrt(n))

    @staticmethod
    def greete():
        print("Hello ")


user = Calculator()
user.greete()
user.findSquare(n=10)
user.findCube(n=2)
user.findRoot(n=64)

"""
📚 Topic: Chapter 11 Exercise - Problem 2

This script demonstrates chapter 11 exercise - problem 2 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 11 exercise - problem 2
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 11 exercise - problem 2 affects the result.
"""


# ‘Pets’. Add a method ‘bark’ to class ‘Dog’
class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    @staticmethod
    def bark():
        print("Dog says bark")


d = Dog()
d.bark()

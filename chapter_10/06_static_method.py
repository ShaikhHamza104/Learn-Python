"""
📚 Topic: Static Methods

This script demonstrates static methods using user input, for loops,
functions and classes.

💡 Key points:
    1️⃣ the basic syntax for static methods
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    static methods affects the result.
"""


class Employee:
    @staticmethod
    def greete():
        print("Welcome")

    def getName(self, name):
        self.name = name
        print(f"Your name is {self.name}")


e1 = Employee()
e1.greete()
name = input("Enter your name : ")
e1.getName(name)

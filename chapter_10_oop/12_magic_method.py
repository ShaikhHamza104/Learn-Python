"""
📚 Topic: Magic Methods (Dunder Methods)

This script demonstrates magic methods (dunder methods) using for loops,
functions and classes.

💡 Key points:
    1️⃣ the basic syntax for magic methods (dunder methods)
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    magic methods (dunder methods) affects the result.
"""


class Employee:
    name = "Hamza"

    def __init__(self):
        pass

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return "This object belong to Employee class"

    def __repr__(self):
        return "Employee()"

    def __call__(self):
        print("Hi ,I am object of this class")


e = Employee()
print(len(e))
print(str(e))
print(repr(e))
e()

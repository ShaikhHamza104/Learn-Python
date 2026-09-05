"""
📚 Topic: Object Introspection

This script demonstrates object introspection using for loops, functions and
classes.

💡 Key points:
    1️⃣ the basic syntax for object introspection
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    object introspection affects the result.
"""


class Person:
    def __init__(self, name, age, qualification):
        self.name = name
        self.age = age
        self.qualification = qualification


a = Person("Hamza", 19, "Diploma Pass")
print(a.__dict__)
print(help(a))

"""
📚 Topic: Method Overriding

This script demonstrates method overriding using for loops, conditions,
functions and classes.

💡 Key points:
    1️⃣ the basic syntax for method overriding
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    method overriding affects the result.
"""


class Enimal:
    # say method is created
    def say(self):
        print("Someting ")


class Dog(Enimal):
    # Override say method for base class
    def say(self):
        print("BOW BOW")


dog = Dog()
dog.say()

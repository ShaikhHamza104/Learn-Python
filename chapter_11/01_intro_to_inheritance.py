"""
📚 Topic: Introduction to Inheritance

This script demonstrates introduction to inheritance using for loops,
functions, classes and imports.

💡 Key points:
    1️⃣ the basic syntax for introduction to inheritance
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    introduction to inheritance affects the result.
"""


# Creating class A
class A:
    def methodA(self):
        print("This method belong to Class A")

# Creating class B


class B(A):
    def methodB(self):
        print("This method belong to Class B")


# Creating class B object
obj = B()

# Calling method for Class A
obj.methodA()

# Calling method for Class b
obj.methodB()

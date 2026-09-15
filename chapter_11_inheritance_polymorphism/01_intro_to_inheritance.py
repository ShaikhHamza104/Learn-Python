"""
📚 Topic: Introduction to Inheritance

This script introduces inheritance, enabling child classes to inherit
attributes and methods from parent classes.

💡 Key points:
    1️⃣ Parent (base) class vs child (derived) class
    2️⃣ Syntax: `class DerivedClass(BaseClass):`
    3️⃣ Reusing code and extending existing functionality

🧠 Beginner tip:
    Inheritance establishes an "is-a" relationship (e.g. a `Dog` is an
    `Animal`).
"""


# Creating class A
class A:
    def method_a(self):
        print("This method belong to Class A")

# Creating class B


class B(A):
    def method_b(self):
        print("This method belong to Class B")


# Creating class B object
obj = B()

# Calling method for Class A
obj.method_a()

# Calling method for Class b
obj.method_b()

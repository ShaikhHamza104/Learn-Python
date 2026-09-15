"""
📚 Topic: Chapter 11 Exercise - Problem 2

Create a multi-level class hierarchy: Animal -> Pets -> Dog, and add a bark
method.

💡 Key points:
    1️⃣ Multi-level inheritance structure
    2️⃣ Subclassing intermediate categories
    3️⃣ Adding specialized behavior at the leaf class
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

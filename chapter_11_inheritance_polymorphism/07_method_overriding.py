"""
📚 Topic: Method Overriding

This script demonstrates method overriding where a subclass provides its own
specialized implementation of a parent class method.

💡 Key points:
    1️⃣ Defining a method in a child class with the same name as in parent
    2️⃣ Child implementation replaces parent behavior for child instances
    3️⃣ Core mechanism enabling runtime polymorphism

🧠 Beginner tip:
    If you need to extend rather than replace parent logic, call
    `super().method()` inside the child override.
"""


class Animal:
    # say method is created
    def say(self):
        print("Something")


class Dog(Animal):
    # Override say method for base class
    def say(self):
        print("BOW BOW")


dog = Dog()
dog.say()

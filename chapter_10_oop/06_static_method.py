"""
📚 Topic: Static Methods (`@staticmethod`)

This script demonstrates static methods that belong to a class namespace but
do not require access to `self` or `cls`.

💡 Key points:
    1️⃣ Decorated with `@staticmethod`
    2️⃣ No automatic `self` or `cls` first argument
    3️⃣ Useful for self-contained helper functions tied to the class domain

🧠 Beginner tip:
    Use `@staticmethod` when a function logically belongs inside a class but
    never touches instance or class state.
"""


class Employee:
    @staticmethod
    def greet():
        print("Welcome")

    def get_name(self, name):
        self.name = name
        print(f"Your name is {self.name}")


e1 = Employee()
e1.greet()
name = input("Enter your name : ")
e1.get_name(name)

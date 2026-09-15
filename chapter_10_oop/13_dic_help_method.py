"""
📚 Topic: Object Introspection with `__dict__` and `help()`

This script demonstrates inspecting instance attributes dynamically using
the `__dict__` attribute and exploring documentation with `help()`.

💡 Key points:
    1️⃣ `obj.__dict__` stores an object's writable attributes as a dictionary
    2️⃣ Viewing class metadata and docstrings with built-in `help()`
    3️⃣ Dynamic attribute inspection during debugging and serialization

🧠 Beginner tip:
    `__dict__` is useful for converting class instances into plain JSON or
    debugging state in unit tests.
"""


class Person:
    def __init__(self, name, age, qualification):
        self.name = name
        self.age = age
        self.qualification = qualification


a = Person("Hamza", 19, "Diploma Pass")
print(a.__dict__)
print(help(a))

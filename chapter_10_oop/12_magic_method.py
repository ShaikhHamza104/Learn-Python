"""
📚 Topic: Special (Dunder / Magic) Methods

This script demonstrates implementing dunder methods (`__str__`, `__len__`,
`__repr__`) to integrate custom objects with Python built-ins.

💡 Key points:
    1️⃣ `__str__`: human-readable string for `print()` and `str()`
    2️⃣ `__len__`: enables Python's built-in `len()` function
    3️⃣ Customizing built-in behaviors on user-defined classes

🧠 Beginner tip:
    Never invent arbitrary dunder names; only implement standard dunders
    defined in Python's data model documentation.
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

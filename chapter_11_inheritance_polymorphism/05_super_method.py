"""
📚 Topic: The `super()` Function

This script demonstrates calling parent class methods and constructors using
Python's built-in `super()` function.

💡 Key points:
    1️⃣ Delegating init to the parent class: `super().__init__()`
    2️⃣ Eliminating hardcoded references to parent class names
    3️⃣ Correctly traversing cooperative MRO hierarchies

🧠 Beginner tip:
    Always call `super().__init__()` in derived class constructors to ensure
    base class state is initialized properly.
"""


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)
        print(a + b)


o = B(10, 20)

"""
📚 Topic: The super() Function

This script demonstrates the super() function using functions and classes.

💡 Key points:
    1️⃣ the basic syntax for the super() function
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    the super() function affects the result.
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

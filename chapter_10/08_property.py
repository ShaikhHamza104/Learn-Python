"""
📚 Topic: Property Decorator

This script demonstrates property decorator using functions and classes.

💡 Key points:
    1️⃣ the basic syntax for property decorator
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    property decorator affects the result.
"""


class MyClass:
    def __init__(self, value):
        self.value = value

    # To access to Function as Value
    @property
    def getValue(self):
        return self.value


o = MyClass(10)
print(o.getValue)

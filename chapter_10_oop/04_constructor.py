"""
📚 Topic: Constructors (`__init__`)

This script demonstrates Python's `__init__` constructor method for
initializing object state automatically upon creation.

💡 Key points:
    1️⃣ The `__init__` method runs automatically whenever an object is created
    2️⃣ Initializes instance state before any other methods are invoked
    3️⃣ Avoids manual setup calls after object creation

🧠 Beginner tip:
    `__init__` cannot return a value; its sole responsibility is initializing
    the newly created instance.
"""


class Constructor:
    def __init__(self):
        print("This is constructor in python")


obj = Constructor()

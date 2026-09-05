"""
📚 Topic: Protected Members

This script demonstrates protected members using for loops, functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for protected members
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    protected members affects the result.
"""


# Create a Base Class
class Base:
    def __init__(self):
        self._name = "Rohan"

# Create a Drived Class


class Drived(Base):
    def __init__(self):
        super().__init__()
        print("Calling protected member of base class:", self._name)

        # Modify the protected variable:
        self._name = "Rohi"
        print("Calling modified protected member outside class:", self._name)


# creating a Object for Drived Class .
d = Drived()

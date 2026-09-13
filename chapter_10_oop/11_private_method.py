"""
📚 Topic: Private Members and Name Mangling

This script demonstrates private members and name mangling using for loops,
functions and classes.

💡 Key points:
    1️⃣ the basic syntax for private members and name mangling
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    private members and name mangling affects the result.
"""


# Create a Base Class
class Base:
    def __init__(self):
        self.__name = "Rohan"

# Create a Drived Class


class Drived(Base):
    def __init__(self):
        super().__init__()
        print("Calling protected member of base class:", self._name)

        # Modify the protected variable:
        self.__name = "Rohi"
        print("Calling modified protected member outside class:", self._name)


# creating a Object for Base Class .
b = Base()
# It will gernate an Attribute Error:
# print(b.__name)

"""
📚 Topic: Private Members & Name Mangling

This script demonstrates the double-underscore prefix (`__member`) for private
members and how Python performs name mangling.

💡 Key points:
    1️⃣ Double-underscore prefix: `__attribute` triggers name mangling
    2️⃣ Python renames `__attr` to `_ClassName__attr` behind the scenes
    3️⃣ Prevents accidental attribute collisions in subclasses

🧠 Beginner tip:
    Private members are not truly private; they can still be reached via
    their mangled name `_ClassName__attribute`.
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

"""
📚 Topic: Protected Members in Python

This script demonstrates the single-underscore convention (`_member`) used to
indicate protected class members intended for internal/subclass use.

💡 Key points:
    1️⃣ Naming convention: prefixing with a single underscore `_attribute`
    2️⃣ Python does not enforce access restrictions; it relies on conventions
    3️⃣ Signals to callers that the attribute is an implementation detail

🧠 Beginner tip:
    "We are all consenting adults here" — Python trusts developers to respect
    conventions rather than locking down variables with compiler errors.
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

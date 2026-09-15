"""
📚 Topic: Single Inheritance

This script demonstrates single inheritance where a derived class inherits
directly from one base class.

💡 Key points:
    1️⃣ Deriving from a single base class
    2️⃣ Overriding base class attributes in the derived class
    3️⃣ Calling inherited and derived methods on child instances

🧠 Beginner tip:
    When an attribute exists in both base and derived classes, the derived
    class attribute takes precedence.
"""


# Creating class A
class A:
    name = "Class A"

    def method_a(self):
        print("This method belong to Class A")
        print(f"My class name is {self.name}")

# B class inheriting the property ,class attribute from class A


class B(A):
    name = "Class B"  # Overide class A attribute eg . name

    def method_b(self):
        print("This method belong to Class B")
        print(f"My class name is {self.name}")


# Creating class B object
obj = B()

# Calling method for Class A
obj.method_a()

# Calling method for Class b
obj.method_b()

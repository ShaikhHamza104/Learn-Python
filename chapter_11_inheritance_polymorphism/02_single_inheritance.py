"""
📚 Topic: Single Inheritance

This script demonstrates single inheritance using for loops, functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for single inheritance
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    single inheritance affects the result.
"""


# Creating class A
class A:
    name = "Class A"

    def methodA(self):
        print("This method belong to Class A")
        print(f"My class name is {self.name}")

# B class inheriting the property ,class attribute from class A


class B(A):
    name = "Class B"  # Overide class A attribute eg . name

    def methodB(self):
        print("This method belong to Class B")
        print(f"My class name is {self.name}")


# Creating class B object
obj = B()

# Calling method for Class A
obj.methodA()

# Calling method for Class b
obj.methodB()

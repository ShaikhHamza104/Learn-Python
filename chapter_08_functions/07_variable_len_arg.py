"""
📚 Topic: Variable-Length Arguments

This script demonstrates variable-length arguments using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for variable-length arguments
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    variable-length arguments affects the result.
"""


def add(*args):
    return sum(args)


result = add(1, 2, 3, 4)  # *args collects all positional arguments into a
# tuple
print(result)  # Output: 10


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Alice", age=30, city="New York")  # **kwargs collects all
# keyword arguments into a dictionary
# Output:
# name: Alice
# age: 30
# city: New York

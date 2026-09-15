"""
📚 Topic: Positional Arguments

This script demonstrates passing arguments based on their ordered position in
the function call.

💡 Key points:
    1️⃣ Mapping caller arguments to parameters by ordinal position
    2️⃣ Order dependency: changing argument order alters assignment
    3️⃣ Enforcing positional-only parameters with `/` (Python 3.8+)

🧠 Beginner tip:
    Keep parameter order intuitive (e.g. `(source, destination)` or
    `(width, height)`).
"""


def add(a, b):
    return a + b


result = add(5, 3)  # Positional arguments: 5 is assigned to a, 3 is assigned
# to b
print(result)  # Output: 8

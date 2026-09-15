"""
📚 Topic: Chapter 11 Exercise - Problem 7

Implement the `__len__()` method on a Vector class to return its dimension.

💡 Key points:
    1️⃣ Implementing `__len__` dunder method
    2️⃣ Returning the length of vector components
    3️⃣ Enabling Python's built-in `len()` function on vector objects
"""


class Vector:
    def __init__(self, components):
        self.components = components

    def __len__(self):
        return len(self.components)


v1 = Vector([1, 2, 3, 8])
print(len(v1))

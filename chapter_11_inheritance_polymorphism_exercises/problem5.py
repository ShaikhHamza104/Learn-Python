"""
📚 Topic: Chapter 11 Exercise - Problem 5

Write a Vector class capable of calculating the sum and dot product of two
vectors.

💡 Key points:
    1️⃣ Overloading `__add__` for vector addition
    2️⃣ Overloading `__mul__` for vector dot product
    3️⃣ Supporting multidimensional vector math
"""


# operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f"{self.x+other.x}+{self.y+other.y}"

    def __mul__(self, other):
        return f"{self.x*other.x}+{self.y*other.y}"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 * v2)

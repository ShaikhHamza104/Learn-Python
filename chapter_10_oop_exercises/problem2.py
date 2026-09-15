"""
📚 Topic: Chapter 10 Exercise - Problem 2

Create a Calculator class capable of finding the square, cube, and square
root of a number.

💡 Key points:
    1️⃣ Implementing arithmetic methods for powers and roots
    2️⃣ Utilizing Python's `math.sqrt()`
    3️⃣ Following PEP 8 snake_case method naming
"""


# Write a class “Calculator” capable of finding square, cube and square root of
# a number.
import math


class Calculator:
    def find_square(self, n):
        print("{} * {} = {}".format(n, n, n**2))

    def find_cube(self, n):
        print("{} * {} * {} = {}".format(n, n, n, n**3))

    def find_root(self, n):
        print(math.sqrt(n))


user = Calculator()
user.find_square(n=10)
user.find_cube(n=2)
user.find_root(n=64)

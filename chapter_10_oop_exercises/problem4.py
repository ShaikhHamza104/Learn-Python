"""
📚 Topic: Chapter 10 Exercise - Problem 4

Add a static greeting method to the Calculator class.

💡 Key points:
    1️⃣ Defining `@staticmethod def greet():`
    2️⃣ Calling static methods on both class and instance
    3️⃣ Combining arithmetic operations with user greetings
"""


import math


class Calculator:
    def find_square(self, n):
        print("{} * {} = {}".format(n, n, n**2))

    def find_cube(self, n):
        print("{} * {} * {} = {}".format(n, n, n, n**3))

    def find_root(self, n):
        print(math.sqrt(n))

    @staticmethod
    def greet():
        print("Hello ")


user = Calculator()
user.greet()
user.find_square(n=10)
user.find_cube(n=2)
user.find_root(n=64)

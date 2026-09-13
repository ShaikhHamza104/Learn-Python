"""
📚 Topic: Chapter 11 Exercise - Problem 4

This script demonstrates chapter 11 exercise - problem 4 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 11 exercise - problem 4
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 11 exercise - problem 4 affects the result.
"""


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __mul__(self, c):
        real_part = self.real * c.real - self.imag * c.imag
        imag_part = self.real * c.imag + self.imag * c.real
        return Complex(real_part, imag_part)

    def __str__(self) -> str:
        return f"{self.real}+{self.imag}i"


# Create instances of Complex
a = Complex(1, 2)
b = Complex(3, 4)

# Print results of addition and multiplication
print(a + b)  # Output: 4+6i
print(a * b)  # Output: -5+10i

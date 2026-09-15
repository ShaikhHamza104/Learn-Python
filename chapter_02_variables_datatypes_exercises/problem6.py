"""
📚 Topic: Exercise 6 - Number Squaring & Exponentiation

This exercise prompts for a number and calculates its square using Python's
exponentiation operator `**`, contrasting it with the bitwise XOR operator `^`.

💡 Key points:
    1️⃣ Calculating powers using the exponentiation operator `**`
    2️⃣ Alternative squaring via self-multiplication (`n * n`)
    3️⃣ Understanding why `^` is bitwise XOR, not exponentiation in Python

🧠 Beginner tip:
    In Python and many other languages, `^` performs bitwise XOR. To raise
    a number to a power, always use `base ** exponent` or `pow(base, exp)`.
"""

num = int(input("Enter a number : "))

# First method
print("The square of the number is", num**2)

# Second method
print("The square of the number is", num * num)

# print("The square of the number is",num^2)#invalid

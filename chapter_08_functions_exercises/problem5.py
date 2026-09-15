"""
📚 Topic: Chapter 08 Exercise - Problem 5

Print an inverted right triangle star pattern recursively.

💡 Key points:
    1️⃣ Base case: stop when `n == 0`
    2️⃣ Printing `n` stars using string multiplication
    3️⃣ Recursive call with `n - 1`
"""


def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)


pattern(3)

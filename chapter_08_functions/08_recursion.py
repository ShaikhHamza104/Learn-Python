"""
📚 Topic: Recursion in Python

This script demonstrates recursive functions that solve problems by calling
themselves with simplified inputs.

💡 Key points:
    1️⃣ Defining a base case to terminate recursion
    2️⃣ Defining a recursive step that moves closer to the base case
    3️⃣ Classic application: computing factorials

🧠 Beginner tip:
    Always verify your base case; missing or unreachable base cases cause
    a `RecursionError` (stack overflow).
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a number : "))
print(f"The factorial of {n} is {factorial(n)}")

"""
📚 Topic: Exercise 1 - Adding Two Input Numbers

This exercise prompts the user to enter two integers in the terminal, casts
the input strings to numbers, and prints their arithmetic sum.

💡 Key points:
    1️⃣ Reading console inputs with `input()`
    2️⃣ Converting string inputs to integers using `int()`
    3️⃣ Computing and displaying the sum with the `+` operator

🧠 Beginner tip:
    Omitting `int()` would concatenate the strings (e.g., '1' + '2' = '12')
    instead of calculating their mathematical sum (3).
"""

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(a + b)

"""
📚 Topic: List Comprehensions

This script demonstrates concise, declarative syntax for building lists
through transformations and filtering.

💡 Key points:
    1️⃣ Basic syntax: `[expression for item in iterable]`
    2️⃣ Conditional filtering: `[expr for item in iterable if condition]`
    3️⃣ Improved readability and performance over manual accumulator loops

🧠 Beginner tip:
    Keep list comprehensions simple and readable; use traditional `for`
    loops if logic becomes multi-line or complex.
"""
# 🔢 Generate 10 elements in a list using list comprehension
# range(1, 11) generates numbers from 1 up to 10.
#
# The last value (11) is NOT included.
#
# So `i` will be:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
li = [i for i in range(1, 11)]

print(li)

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 🟢 Generate even numbers from 10 to 40
# range(10, 41) generates numbers from 10 to 40.
#
# `i % 2 == 0` checks whether a number is even.
# `%` gives us the remainder after division.
#
# If the remainder is 0 when dividing by 2,
# the number is even.
l2 = [i for i in range(10, 41) if i % 2 == 0]

print(l2)

# Output:
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
#  30, 32, 34, 36, 38, 40]


# 🟠 Generate odd numbers from 10 to 20
# range(10, 21) generates numbers from 10 to 20.
#
# `i % 2 != 0` checks whether the number is odd.
# If the remainder is NOT 0 after dividing by 2,
# the number is odd.
l3 = [i for i in range(10, 21) if i % 2 != 0]

print(l3)

# Output:
# [11, 13, 15, 17, 19]

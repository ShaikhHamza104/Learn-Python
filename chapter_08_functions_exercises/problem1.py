"""
📚 Topic: Chapter 08 Exercise - Problem 1

Write a function to find and return the greatest of three numbers.

💡 Key points:
    1️⃣ Defining a function accepting three parameters
    2️⃣ Comparing values using conditional logic
    3️⃣ Returning the maximum value
"""


def greatest(a, b, c):
    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b

    else:
        return c


g = greatest(10, 89, 100)
print(g)

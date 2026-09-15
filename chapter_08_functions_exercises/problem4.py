"""
📚 Topic: Chapter 08 Exercise - Problem 4

Write a recursive function to calculate the sum of the first `n` natural
numbers.

💡 Key points:
    1️⃣ Base case: when `n == 1`, return 1
    2️⃣ Recursive step: return `func(n - 1) + n`
    3️⃣ Demonstrating call stack accumulation
"""


def recursive_sum(n):
    if n == 1:
        return 1
    return recursive_sum(n - 1) + n


n = int(input("Enter a number : "))
print(recursive_sum(n))

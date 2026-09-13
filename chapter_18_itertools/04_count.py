"""
📚 Topic: count

This script demonstrates count from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import count, islice

# ============================================================
# 1. BASIC COUNT
# ============================================================
print("=" * 60)
print("1. BASIC COUNT")
print("=" * 60)

numbers = count(10, 2)
print("First five values:", list(islice(numbers, 5)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("count examples completed!")
print("=" * 60)

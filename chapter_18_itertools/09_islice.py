"""
📚 Topic: islice

This script demonstrates islice from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import islice

# ============================================================
# 1. BASIC ISLICE
# ============================================================
print("=" * 60)
print("1. BASIC ISLICE")
print("=" * 60)

numbers = range(1, 11)
print("First five:", list(islice(numbers, 5)))


# ============================================================
# 2. START, STOP AND STEP
# ============================================================
print("\n" + "=" * 60)
print("2. START, STOP AND STEP")
print("=" * 60)

numbers = range(1, 11)
print("Selected:", list(islice(numbers, 1, 9, 2)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("islice examples completed!")
print("=" * 60)

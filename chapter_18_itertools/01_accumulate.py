"""
📚 Topic: accumulate

This script demonstrates accumulate from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import accumulate

# ============================================================
# 1. BASIC ACCUMULATE
# ============================================================
print("=" * 60)
print("1. BASIC ACCUMULATE")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)
print("Accumulated:", list(accumulate(numbers)))


# ============================================================
# 2. ACCUMULATE WITH A FUNCTION
# ============================================================
print("\n" + "=" * 60)
print("2. ACCUMULATE WITH A FUNCTION")
print("=" * 60)

result = accumulate(numbers, lambda x, y: x * y)
print("Product accumulation:", list(result))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("accumulate examples completed!")
print("=" * 60)

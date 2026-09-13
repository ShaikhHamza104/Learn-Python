"""
📚 Topic: tee

This script demonstrates tee from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import tee

# ============================================================
# 1. BASIC TEE
# ============================================================
print("=" * 60)
print("1. BASIC TEE")
print("=" * 60)

numbers = iter([1, 2, 3, 4, 5])
first, second = tee(numbers)

print("First iterator:", list(first))
print("Second iterator:", list(second))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("tee examples completed!")
print("=" * 60)

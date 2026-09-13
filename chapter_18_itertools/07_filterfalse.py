"""
📚 Topic: filterfalse

This script demonstrates filterfalse from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import filterfalse

# ============================================================
# 1. BASIC FILTERFALSE
# ============================================================
print("=" * 60)
print("1. BASIC FILTERFALSE")
print("=" * 60)

numbers = range(1, 11)
print("Odd numbers:", list(filterfalse(lambda x: x % 2 == 0, numbers)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("filterfalse examples completed!")
print("=" * 60)

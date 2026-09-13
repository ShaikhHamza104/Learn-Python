"""
📚 Topic: takewhile

This script demonstrates takewhile from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import takewhile

# ============================================================
# 1. BASIC TAKEWHILE
# ============================================================
print("=" * 60)
print("1. BASIC TAKEWHILE")
print("=" * 60)

numbers = [1, 2, 3, 4, 1, 2]
print("Numbers:", numbers)
print("Result:", list(takewhile(lambda x: x < 4, numbers)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("takewhile examples completed!")
print("=" * 60)

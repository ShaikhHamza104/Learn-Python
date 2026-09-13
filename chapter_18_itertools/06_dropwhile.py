"""
📚 Topic: dropwhile

This script demonstrates dropwhile from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import dropwhile

# ============================================================
# 1. BASIC DROPWHILE
# ============================================================
print("=" * 60)
print("1. BASIC DROPWHILE")
print("=" * 60)

numbers = [1, 2, 3, 4, 1, 2]
print("Numbers:", numbers)
print("Result:", list(dropwhile(lambda x: x < 3, numbers)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("dropwhile examples completed!")
print("=" * 60)

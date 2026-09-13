"""
📚 Topic: cycle

This script demonstrates cycle from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import cycle, islice

# ============================================================
# 1. BASIC CYCLE
# ============================================================
print("=" * 60)
print("1. BASIC CYCLE")
print("=" * 60)

values = cycle(["A", "B", "C"])
print("First eight values:", list(islice(values, 8)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("cycle examples completed!")
print("=" * 60)

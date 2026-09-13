"""
📚 Topic: compress

This script demonstrates compress from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import compress

# ============================================================
# 1. BASIC COMPRESS
# ============================================================
print("=" * 60)
print("1. BASIC COMPRESS")
print("=" * 60)

data = ["A", "B", "C", "D", "E"]
selectors = [1, 0, 1, 0, 1]

print("Data:", data)
print("Selectors:", selectors)
print("Selected:", list(compress(data, selectors)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("compress examples completed!")
print("=" * 60)

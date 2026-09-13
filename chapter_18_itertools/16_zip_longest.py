"""
📚 Topic: zip_longest

This script demonstrates zip_longest from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import zip_longest

# ============================================================
# 1. BASIC ZIP_LONGEST
# ============================================================
print("=" * 60)
print("1. BASIC ZIP_LONGEST")
print("=" * 60)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]

result = zip_longest(names, ages, fillvalue="N/A")

print("Names:", names)
print("Ages:", ages)
print("Combined:", list(result))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("zip_longest examples completed!")
print("=" * 60)

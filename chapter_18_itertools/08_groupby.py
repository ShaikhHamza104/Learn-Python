"""
📚 Topic: groupby

This script demonstrates groupby from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import groupby

# ============================================================
# 1. BASIC GROUPBY
# ============================================================
print("=" * 60)
print("1. BASIC GROUPBY")
print("=" * 60)

words = ["apple", "ant", "banana", "boat", "cat", "car"]
words.sort(key=lambda word: word[0])

for key, group in groupby(words, key=lambda word: word[0]):
    print(key, list(group))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("groupby examples completed!")
print("=" * 60)

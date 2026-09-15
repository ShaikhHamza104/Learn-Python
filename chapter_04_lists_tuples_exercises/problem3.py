"""
📚 Topic: Chapter 04 Exercise - Problem 3

Demonstrate that tuple elements cannot be changed once defined (immutability).

💡 Key points:
    1️⃣ Creating a heterogeneous tuple
    2️⃣ Verifying immutability when attempting item reassignment
    3️⃣ Understanding Python's `TypeError` on tuple modification
"""
# 📦 Create a tuple with different types of values
t = (1, 2, 3, True, None)


# ❌ Try to change the first element of the tuple
# Tuples are immutable, so we cannot change their elements.
#
# If we remove the `#` and run this line, Python will give a TypeError.
# This happens because `t[0]` cannot be assigned a new value.
#
# t[0] = 90


# 💡 Beginner tip:
# Lists are mutable, so their elements can be changed.
# Tuples are immutable, so their elements cannot be changed.

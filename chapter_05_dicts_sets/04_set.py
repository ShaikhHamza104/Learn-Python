"""
📚 Topic: Python Sets

This script introduces sets as unordered collections of unique, hashable
elements.

💡 Key points:
    1️⃣ Creating an empty set using `set()` (not `{}`)
    2️⃣ Automatic deduplication of duplicate elements
    3️⃣ Unordered nature: sets do not preserve insertion order or indexing

🧠 Beginner tip:
    Writing `{}` creates an empty dictionary, not an empty set. Always use
    `set()` to initialize an empty set.
"""
# 📦 Creating an empty set
# `set()` creates an empty set.
e = set()

# 🔍 Check the type of `e`
# This confirms that `e` is a set.
print(type(e))

# Output:
# <class 'set'>


# 🔢 Creating a set with multiple values
# Here, we create a set containing several numbers.
s = {1, 2, 3, 4, 5, 89, 10}


# 🔍 Print the set and its type
# `type(s)` confirms that `s` is a set.
print(s, type(s))

# Output:
# {1, 2, 3, 4, 5, 89, 10} <class 'set'>

# 💡 Remember:
# Sets contain unique values and do not support indexing like lists.

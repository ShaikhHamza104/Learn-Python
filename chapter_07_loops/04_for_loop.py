"""
📚 Topic: The `for` Loop

This script demonstrates idiomatic iteration across sequences (lists, tuples,
strings) using Python's `for...in` syntax.

💡 Key points:
    1️⃣ Direct element iteration without manual indexing
    2️⃣ Traversing lists, tuples, and individual string characters
    3️⃣ Clean, readable, and safe against out-of-bounds index errors

🧠 Beginner tip:
    Python's `for` loop is actually a `for-each` loop, pulling items from an
    iterable until exhausted.
"""
# ═══════════════════════════════════════
# 🔤 for Loop with String
# ═══════════════════════════════════════

s = "Hamza"

# 🔄 Get each character from the string
for char in s:
    print(char)


# ═══════════════════════════════════════
# 📋 for Loop with List
# ═══════════════════════════════════════

l = [1, 2, 3, "Harry", "Rohan", "Rahul"]  # noqa: E741

# 🔄 Get each element from the list
for e in l:
    print(e)


# ═══════════════════════════════════════
# 📦 for Loop with Tuple
# ═══════════════════════════════════════

t = (0, 1, 2, 4, 56, 75, 13)

# 🔄 Get each element from the tuple
for i in t:
    print(i)

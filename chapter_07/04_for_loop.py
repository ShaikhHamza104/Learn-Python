"""
📚 Topic: For Loop

This script demonstrates for loop using for loops.

💡 Key points:
    1️⃣ the basic syntax for for loop
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    for loop affects the result.
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

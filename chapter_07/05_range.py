"""
📚 Topic: Range

This script demonstrates range using for loops.

💡 Key points:
    1️⃣ the basic syntax for range
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    range affects the result.
"""


# 🔢 Create a range from 0 to 6
a = range(7)

# 🔄 Print each number from the range
for i in a:
    print(i)


# ═══════════════════════════════════════
# 🟡 Printing Odd Numbers
# ═══════════════════════════════════════

# Start at 1, stop before 10, and increase by 2
for i in range(1, 10, 2):
    print(i)

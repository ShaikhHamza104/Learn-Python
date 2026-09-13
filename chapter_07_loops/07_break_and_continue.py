"""
📚 Topic: Break And Continue

This script demonstrates break and continue using for loops and conditions.

💡 Key points:
    1️⃣ the basic syntax for break and continue
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    break and continue affects the result.
"""


# ═══════════════════════════════════════
# 🛑 Using break
# ═══════════════════════════════════════

for i in range(80):
    # Stop the loop when i becomes 8
    if i == 8:
        break

    print(i)


# ═══════════════════════════════════════
# ⏭️ Using continue
# ═══════════════════════════════════════

for i in range(80):
    # Skip 8 and continue with the next number
    if i == 8:
        continue

    print(i)


# ═══════════════════════════════════════
# 🔢 Printing Even Numbers
# ═══════════════════════════════════════

for i in range(1, 90):
    # If number is odd, skip it
    if i % 2 == 1:
        continue

    # Only even numbers reach this line
    print(i)

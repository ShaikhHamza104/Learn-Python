"""
📚 Topic: Pass

This script demonstrates pass using for loops and while loops.

💡 Key points:
    1️⃣ the basic syntax for pass
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    pass affects the result.
"""


# ═══════════════════════════════════════
# 💤 Using pass
# ═══════════════════════════════════════

# `pass` does nothing, so this loop produces no output
for i in range(1, 90):
    pass


# ═══════════════════════════════════════
# 🔄 Using while Loop
# ═══════════════════════════════════════

# Start counting from 1
i = 1

# Continue while i is less than or equal to 10
while i <= 10:
    print(i)

    # Increase i by 1 after every iteration
    i += 1

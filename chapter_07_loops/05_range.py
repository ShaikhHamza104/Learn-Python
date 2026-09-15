"""
📚 Topic: The `range()` Function

This script demonstrates generating arithmetic progressions with `range()`
for numeric loop iteration.

💡 Key points:
    1️⃣ Single argument: `range(stop)` (0 up to stop, exclusive)
    2️⃣ Two arguments: `range(start, stop)`
    3️⃣ Three arguments: `range(start, stop, step)` for custom stride

🧠 Beginner tip:
    `range()` produces numbers lazily on demand, making it memory-efficient
    even for millions of steps.
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

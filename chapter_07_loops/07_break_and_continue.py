"""
📚 Topic: Loop Control: `break` and `continue`

This script demonstrates altering loop flow using `break` to exit early and
`continue` to skip the remainder of the current iteration.

💡 Key points:
    1️⃣ `break`: immediately halts and exits the enclosing loop
    2️⃣ `continue`: skips remaining statements in current turn and advances
    3️⃣ Controlling loop lifecycle conditionally

🧠 Beginner tip:
    Use `break` to exit once a search target is found; use `continue` to
    bypass invalid or irrelevant data items.
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

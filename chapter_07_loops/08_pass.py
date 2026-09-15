"""
📚 Topic: The `pass` Statement

This script demonstrates using `pass` as a syntactic placeholder in loops,
functions, and condition blocks.

💡 Key points:
    1️⃣ `pass` is a null statement (no-op)
    2️⃣ Satisfies Python's requirement for non-empty indented code blocks
    3️⃣ Commonly used as a temporary placeholder during development

🧠 Beginner tip:
    Use `pass` when outlining code architecture before implementing
    detailed logic.
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

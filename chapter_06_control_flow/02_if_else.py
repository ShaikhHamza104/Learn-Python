"""
📚 Topic: Two-Way Branching with `if-else`

This script demonstrates two-way branching using `if-else` blocks to handle
both True and False condition outcomes.

💡 Key points:
    1️⃣ Executing the `if` branch when condition is True
    2️⃣ Falling back to the `else` block when condition is False
    3️⃣ Exactly one branch is guaranteed to execute

🧠 Beginner tip:
    An `else` block cannot stand alone; it must always be paired with a
    preceding `if` statement.
"""
# 👤 Ask the user to enter their age
age = int(input("Enter your age: "))

# 🔍 Check whether the person is under 18
if age < 18:
    print("You cannot vote")

# ✅ If age is 18 or above
else:
    print("You can vote")

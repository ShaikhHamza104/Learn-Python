"""
📚 Topic: Multi-Way Branching with `if-elif-else`

This script demonstrates chaining multiple conditions using `elif` (else-if)
ladders to test sequential possibilities.

💡 Key points:
    1️⃣ Testing sequential conditions from top to bottom
    2️⃣ Short-circuit execution: once a condition is True, remaining tests skip
    3️⃣ Providing an optional final `else` fallback for unmatched cases

🧠 Beginner tip:
    Order your conditions carefully. The first condition that evaluates to
    True wins, even if later conditions would also be True.
"""
# 👤 Ask the user to enter their age
age = int(input("Enter your age: "))

# ❌ Check for invalid age first
if age <= 0:
    print("Your age is invalid.....")

# 🔞 Check if the person is under 18
elif age < 18:
    print("You cannot vote")

# ✅ If age is 18 or above
else:
    print("You can vote")

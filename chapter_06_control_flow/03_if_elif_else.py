"""
📚 Topic: If Elif Else

This script demonstrates if elif else using conditions and user input.

💡 Key points:
    1️⃣ the basic syntax for if elif else
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    if elif else affects the result.
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

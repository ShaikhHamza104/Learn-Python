"""
📚 Topic: Chapter 07 Exercise - Problem 5

This script demonstrates chapter 07 exercise - problem 5 using user input,
while loops and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 5
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 5 affects the result.
"""


# 🔢 Take the value of n from the user
num = int(input("Enter number: "))

# ▶️ Start the counter from 0
i = 0

# 📦 Variable to store the total
total = 0

# 🔄 Add numbers from 0 to num
while i <= num:
    # ➕ Add the current number to total
    total += i

    # ⏭️ Move to the next number
    i += 1

# ✅ Display the final result
print(f"Sum of {num} natural numbers is {total}")

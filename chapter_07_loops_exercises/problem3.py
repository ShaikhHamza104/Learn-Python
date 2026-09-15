"""
📚 Topic: Chapter 07 Exercise - Problem 3

Print the multiplication table of a user-specified number using a `while` loop.

💡 Key points:
    1️⃣ Initializing loop counter at 1
    2️⃣ Running `while` loop until multiplier reaches 10
    3️⃣ Incrementing counter explicitly in each iteration
"""
# 🔢 Take a number from the user
num = int(input("Enter a number: "))

# ▶️ Start the counter from 1
i = 1

# 🔄 Run the loop until i reaches 11
while i < 11:
    # ✖️ Print the multiplication result
    print(f"{num} x {i} = {num * i}")

    # ➕ Increase i by 1
    i += 1

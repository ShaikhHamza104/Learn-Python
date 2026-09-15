"""
📚 Topic: Chapter 07 Exercise - Problem 5

Calculate the sum of the first `n` natural numbers using a `while` loop.

💡 Key points:
    1️⃣ Initializing accumulator total to 0
    2️⃣ Iterating while counter is less than or equal to `n`
    3️⃣ Adding counter to accumulator and printing final sum
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

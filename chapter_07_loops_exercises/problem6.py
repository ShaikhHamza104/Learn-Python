"""
📚 Topic: Chapter 07 Exercise - Problem 6

Calculate the factorial of a given number using a `for` loop.

💡 Key points:
    1️⃣ Initializing factorial product accumulator to 1
    2️⃣ Iterating from 1 through `n` with `range(1, n + 1)`
    3️⃣ Multiplying running product by current iteration value
"""
# 🔢 Take a number from the user
num = int(input("Enter number: "))

# 📦 Start the factorial result with 1
fact = 1

# 🔄 Loop from 1 to num
for i in range(1, num + 1):
    # ✖️ Multiply the current result by i
    fact = fact * i

# ✅ Display the final factorial
print(f"Factorial of {num} is {fact}")

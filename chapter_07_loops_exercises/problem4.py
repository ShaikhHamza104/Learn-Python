"""
📚 Topic: Chapter 07 Exercise - Problem 4

This script demonstrates chapter 07 exercise - problem 4 using user input,
for loops, conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 4
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 4 affects the result.
"""


# 🔢 Take a number from the user
n = int(input("Enter number: "))

# 🔍 Check whether n is divisible by any number from 2 to n-1
for i in range(2, n):
    # If remainder is 0, n is exactly divisible by i
    if n % i == 0:
        # ❌ A number with another factor is not prime
        print("Given number is not prime")

        # 🛑 Stop checking further
        break

# ✅ This runs only if the loop was not stopped by break
else:
    print("Given number is prime")

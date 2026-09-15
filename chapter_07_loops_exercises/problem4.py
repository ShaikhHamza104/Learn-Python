"""
📚 Topic: Chapter 07 Exercise - Problem 4

Determine whether a given number is prime using a `for-else` loop.

💡 Key points:
    1️⃣ Checking divisibility from 2 up to `n - 1`
    2️⃣ Breaking early when a factor is found
    3️⃣ Leveraging `else` block to confirm prime numbers
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

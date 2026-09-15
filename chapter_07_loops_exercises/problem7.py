"""
📚 Topic: Chapter 07 Exercise - Problem 7

Print an centered pyramid star pattern of `n` rows.

💡 Key points:
    1️⃣ Calculating leading spaces for row centering: `n - i`
    2️⃣ Calculating odd star counts per row: `2 * i - 1`
    3️⃣ Combining string repetition and concatenation
"""
# 🔢 Take the number of rows from the user
n = int(input("Enter a number: "))

# 🔄 Create each row of the pattern
for i in range(1, n + 1):

    # ⬜ Print spaces before the stars
    # `end=""` prevents moving to the next line
    print(" " * (n - i), end="")

    # ⭐ Print the required number of stars
    print("*" * (2 * i - 1), end="")

    # ↩️ Move to the next line
    print("")

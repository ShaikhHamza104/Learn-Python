"""
📚 Topic: Leap Year

This script demonstrates leap year using conditions and user input.

💡 Key points:
    1️⃣ the basic syntax for leap year
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    leap year affects the result.
"""


# 📅 Take the year from the user
year = int(input("Enter year: "))

# 🔍 First, check whether the year is divisible by 4
if year % 4 == 0:
    # 🔍 If yes, check whether the year is divisible by 100
    if year % 100 == 0:
        # 🔍 If yes, it must also be divisible by 400
        if year % 400 == 0:
            print("Year is a leap year")

        # ❌ Divisible by 100 but not by 400
        else:
            print("Year is not a leap year")

    # ✅ Divisible by 4 but not by 100
    else:
        print("Year is a leap year")

# ❌ Not divisible by 4
else:
    print("Year is not a leap year")

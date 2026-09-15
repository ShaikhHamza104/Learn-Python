"""
📚 Topic: Leap Year Logic with Compound Conditions

This script implements leap year determination rules using boolean operators
(`and`, `or`) and nested conditional logic.

💡 Key points:
    1️⃣ A year is a leap year if divisible by 4 and not by 100
    2️⃣ Century years must also be divisible by 400 to qualify
    3️⃣ Combining multiple boolean checks into a single expression

🧠 Beginner tip:
    Use parentheses when mixing `and` and `or` operators to ensure logical
    grouping is clear and unambiguous.
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

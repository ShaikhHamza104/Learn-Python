"""
📚 Topic: Multiple Independent `if` Statements

This script demonstrates independent `if` statements where each condition
is evaluated separately, unlike an `if-elif-else` ladder.

💡 Key points:
    1️⃣ Independent evaluation: every `if` statement is evaluated
    2️⃣ Multiple blocks can execute if multiple conditions are True
    3️⃣ Comparing independent `if` vs exclusive `elif` ladders

🧠 Beginner tip:
    Use `if-elif` when only one outcome should occur; use multiple `if`
    statements when multiple conditions can independently apply.
"""
# 📏 Ask the user for their height
height = int(input("Enter your height in cm: "))

# 💰 Start the bill at $0
bill = 0

# 🎢 Check if the person is tall enough to ride
if height >= 120:
    print("You can ride")

    # 👤 Ask for the user's age
    age = int(input("Enter your age: "))

    # 👶 Ticket price for children under 12
    if age < 12:
        print("You have to pay $5")
        bill = 5

    # 🧒 Ticket price for ages 12 to 18
    elif age <= 18:
        print("You have to pay $7")
        bill = 7

    # 🧑 Ticket price for people above 18
    else:
        print("You have to pay $12")
        bill = 12

    # 📸 Ask if the user wants a photo
    photo = input("Do you want to take a photo? ")

    # ➕ Add $3 if the user wants a photo
    if photo == "yes" or photo == "y":
        print("You have to pay an extra $3")
        bill += 3

    # 🧾 Display the final bill
    print(f"Your total bill is ${bill}")

# ❌ Person is not tall enough
else:
    print("You cannot ride")

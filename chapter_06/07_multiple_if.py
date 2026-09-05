"""
📚 Topic: Multiple If

This script demonstrates multiple if using conditions and user input.

💡 Key points:
    1️⃣ the basic syntax for multiple if
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    multiple if affects the result.
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

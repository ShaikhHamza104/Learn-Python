"""
📚 Topic: 02 Multiple Except Block

This script demonstrates 02 multiple except block using user input, while
loops and exception handling.

💡 Key points:
    1️⃣ the basic syntax for 02 multiple except block
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    02 multiple except block affects the result.
"""

l = [1, 2, 3, 4]  # noqa: E741
try:
    user_input = int(input("Enter a number between 0 and 3: "))
    i = 0
    while i < user_input:
        print(l[user_input])
        i += 1
except ValueError:
    print("Enter a valid number not character or floting point number")
except IndexError:
    print("Enter value not be grater then ", len(l) - 1)

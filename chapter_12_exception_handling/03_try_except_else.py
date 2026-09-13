"""
📚 Topic: 03 Try Except Else

This script demonstrates 03 try except else using user input, for loops,
conditions and exception handling.

💡 Key points:
    1️⃣ the basic syntax for 03 try except else
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    03 try except else affects the result.
"""


try:
    n = int(input("Enter a number you want to print table: "))

except ValueError:
    print("Enter a valid number. Neither floating point number nor character ")

except Exception as e:
    print(e)

else:
    for i in range(1, 11, 1):
        print(f"{n} X {i} = {n*i}")

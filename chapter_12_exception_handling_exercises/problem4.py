"""
📚 Topic: Problem4

This script demonstrates problem4 using user input, for loops, conditions
and functions.

💡 Key points:
    1️⃣ the basic syntax for problem4
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem4 affects the result.
"""


# Implement file operations and use finally to close the file even when
# an exception occurs.
def openFile(file_name):
    try:
        with open(file_name, "r") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("File is not available yet.")
    finally:
        f.close()


def writeFile(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)


try:
    user = int(
        input("""
1. Open an existing file
2. Write to a file
Choose an option: """)
    )

    file_name = input("Enter the file name: ")
    if user == 1:
        openFile(file_name)
    elif user == 2:
        data = input("Input some data for the file: ")
        writeFile(file_name, data)
    else:
        print("Invalid option chosen.")
except ValueError:
    print("Invalid input. Please enter a number.")

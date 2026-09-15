"""
📚 Topic: Chapter 12 Exercise - Problem 4

Implement file reading and writing with exception safety and error handling.

💡 Key points:
    1️⃣ Safe file opening with `try-except`
    2️⃣ Catching `FileNotFoundError`
    3️⃣ Exception-safe resource management
"""


# Implement file operations and use finally to close the file even when
# an exception occurs.
def open_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("File is not available yet.")


def write_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
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
        open_file(file_name)
    elif user == 2:
        data = input("Input some data for the file: ")
        write_file(file_name, data)
    else:
        print("Invalid option chosen.")
except ValueError:
    print("Invalid input. Please enter a number.")

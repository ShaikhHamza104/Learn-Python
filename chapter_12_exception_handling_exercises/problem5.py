"""
📚 Topic: Chapter 12 Exercise - Problem 5

Copy content from one file to another, catching `FileNotFoundError` and
`PermissionError`.

💡 Key points:
    1️⃣ Reading source file and writing to destination file
    2️⃣ Catching missing source files
    3️⃣ Handling permission denied errors gracefully
"""


# Read one file and write its content to another. Handle errors such as
# a missing file or denied permission.
try:
    source_file = input("Enter a file name: ")
    with open(source_file, "r", encoding="utf-8") as f:
        data = f.read()
    copy_file = input("Choose your copy file name : ")
    with open(copy_file, "w", encoding="utf-8") as f:
        f.write(data)
except FileNotFoundError:
    print("File is not available yet.")

except PermissionError:
    print("You can not handle this tasks.")

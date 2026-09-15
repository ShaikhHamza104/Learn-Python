"""
📚 Topic: Safe File Handling with Exceptions

This script demonstrates safely opening and reading files with exception
guards against missing files.

💡 Key points:
    1️⃣ Catching `FileNotFoundError` when accessing filesystem resources
    2️⃣ Preventing unbound variable errors in cleanup blocks
    3️⃣ Releasing file handles cleanly

🧠 Beginner tip:
    Prefer `with open(...)` which automatically and safely closes files even
    when exceptions are raised.
"""


f = None
filename = input("Enter file name you want to open: ")
try:
    f = open(filename, "r", encoding="utf-8")
except FileNotFoundError:
    print(f"'{filename}' not found error")
else:
    data = f.read()
    print(data)
finally:
    if f is not None:
        f.close()

"""
📚 Topic: String Creation & Indexing

This script demonstrates string literal declarations (single, double, and
triple quotes) and character indexing with both positive and negative
offsets.

💡 Key points:
    1️⃣ Declaring strings with `'...'`, `"..."`, or triple quotes
    2️⃣ Accessing characters via 0-based positive indexing (`s[0]`, `s[1]`)
    3️⃣ Accessing characters from the end using negative indexing (`s[-1]`)

🧠 Beginner tip:
    Python strings are immutable: once created in memory, individual
    characters cannot be mutated (e.g., `s[0] = 'X'` raises a TypeError).
"""

# string using single quotes:
string = "This is string"

# string using double quotes:
string = "This is string"

# string using three quotes:
string = """This
is
string"""

name = "Hamza"
# Positive indexes
print(name[0])  # print the first character "H"
print(name[1])
print(name[2])
print(name[3])

# negative indexes
print(name[-1])  # print the last character "a"
print(name[-2])
print(name[-3])

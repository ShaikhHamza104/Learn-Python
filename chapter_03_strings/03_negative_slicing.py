"""
📚 Topic: Negative Index Slicing

This script demonstrates slicing strings using negative index boundaries,
extracting substrings relative to the end of the text.

💡 Key points:
    1️⃣ Negative indices start at `-1` for the last character
    2️⃣ Specifying slices with negative ranges: `str[-4:-1]`
    3️⃣ Calculating equivalent positive index boundaries

🧠 Beginner tip:
    To translate a negative index `-k` to a positive index, simply add the
    string length: `len(str) + (-k)`.
"""

name = "Hamza"
#     012345
print(name[-4:-1])  # amza
print(name[-2:-1])  # z

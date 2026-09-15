"""
📚 Topic: String Slicing & Stride Syntax

This script demonstrates slicing sequences using `str[start:end]` and step
strides `str[start:end:step]` to extract specific substrings.

💡 Key points:
    1️⃣ Basic slicing syntax: `str[start:end]` (exclusive of end index)
    2️⃣ Omitting boundaries: `str[:end]` or `str[start:]`
    3️⃣ Using step intervals: `str[start:end:step]` to skip characters

🧠 Beginner tip:
    The stop index in Python slicing is always *exclusive*. For example,
    `"Python"[0:2]` extracts characters at index 0 and 1, returning `"Py"`.
"""

name = "Hamza"
# str[start:end]
print(name[0:3])  # Ham
print(name[1:4])  # amz
print(name[1:])  # amza
print(name[:])  # Hamza

word = "Amazing"
#     0123456
#      1  1  1
# str[start:end:step]
print(word[1:4:2])  # mz
print(word[1:6:3])  # mi

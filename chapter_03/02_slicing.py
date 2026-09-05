"""
📚 Topic: Slicing

This script demonstrates slicing using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for slicing
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    slicing affects the result.
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

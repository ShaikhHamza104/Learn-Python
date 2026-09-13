"""
📚 Topic: Appending to Files

This script demonstrates appending to files using file or path operations.

💡 Key points:
    1️⃣ the basic syntax for appending to files
    2️⃣ how file or path operations fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    appending to files affects the result.
"""


f = open('random.txt', 'a')

# writing to a file
data = "\nThis is some more about it "
f.write(data)

# printing data in file
print(data)

# closeing to a file
f.close()

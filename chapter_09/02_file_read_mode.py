"""
📚 Topic: Reading Files

This script demonstrates reading files using file or path operations.

💡 Key points:
    1️⃣ the basic syntax for reading files
    2️⃣ how file or path operations fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    reading files affects the result.
"""


# Opening a file
f = open('sample.txt', 'r')

# reading to a file
data = f.read()

# printing data in file
print(data)

# closeing to a file
f.close()


# Opening a file
f = open('sample.txt', 'r')

# reading  one line file using readline
data = f.readline()

# printing data in file
print(data)

# closeing to a file
f.close()


# Opening a file
f = open('sample.txt', 'r')

# reading  file in a form of list  using readlines
data = f.readlines()

# printing data in file
print(data)

# closeing to a file
f.close()

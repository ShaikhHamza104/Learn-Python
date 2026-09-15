"""
📚 Topic: Reading Files Line by Line

This script demonstrates reading files using explicit `'r'` mode and methods
like `readline()` and `readlines()`.

💡 Key points:
    1️⃣ Explicit `'r'` mode flag
    2️⃣ `readline()`: reads a single line at a time
    3️⃣ `readlines()`: loads all lines into a list of strings

🧠 Beginner tip:
    For large files, iterating directly over the file object (`for line in f:`)
    is memory-efficient because it streams lines one at a time.
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

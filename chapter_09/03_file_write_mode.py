"""
📚 Topic: Writing to Files

This script demonstrates writing to files using file or path operations.

💡 Key points:
    1️⃣ the basic syntax for writing to files
    2️⃣ how file or path operations fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    writing to files affects the result.
"""


# Opening a file
f = open('random.txt', 'w')

# writing to a file
data = "I am using File i/o"
f.write(data)

# printing data in file
print(data)

# closeing to a file
f.close()


# Opening a file
f = open('random.txt', 'w')

# writing to a file using writelines
data = "I am using File i/o"
f.writelines(data)

# printing data in file
print(data)

# closeing to a file
f.close()

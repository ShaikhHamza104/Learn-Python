"""
📚 Topic: Exclusive Creation Mode

This script demonstrates exclusive creation mode using user input and file
or path operations.

💡 Key points:
    1️⃣ the basic syntax for exclusive creation mode
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    exclusive creation mode affects the result.
"""


# 'x' mode give error if file is alrady exisist
# open a file in x mode
f = open("random1.txt", 'x')

# data input from the user
data = input("Enter data")

# writing to a file
f.write(data)

# printing data
print(data)

# closing to a file
f.close()

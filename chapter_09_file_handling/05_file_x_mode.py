"""
📚 Topic: Exclusive Creation Mode (`'x'`)

This script demonstrates exclusive file creation mode (`'x'`), which creates a
file only if it does not already exist.

💡 Key points:
    1️⃣ `'x'` mode opens a file for exclusive writing
    2️⃣ If the file already exists, Python raises `FileExistsError`
    3️⃣ Prevents accidental overwriting of existing critical data

🧠 Beginner tip:
    Use `'x'` mode when generating unique output files to guarantee no
    previous file is destroyed.
"""
# 'x' mode raises an error if the file already exists
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

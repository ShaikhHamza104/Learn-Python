"""
📚 Topic: Writing Files with `'w'` Mode

This script demonstrates writing text to files using write mode (`'w'`).

💡 Key points:
    1️⃣ `'w'` mode creates the file if it does not exist
    2️⃣ Truncation warning: `'w'` completely overwrites existing content
    3️⃣ Writing strings with `f.write(data)`

🧠 Beginner tip:
    `f.write()` does not automatically append a newline; add `\n` manually
    when line breaks are desired.
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

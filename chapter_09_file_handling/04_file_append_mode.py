"""
📚 Topic: Appending to Files with `'a'` Mode

This script demonstrates appending content to an existing file without
overwriting its previous contents.

💡 Key points:
    1️⃣ `'a'` mode places the file pointer at the end of the file
    2️⃣ Preserves existing data while adding new lines
    3️⃣ Creates the file if it does not yet exist

🧠 Beginner tip:
    Use `'a'` mode for audit logs, activity trackers, and incremental records.
"""
f = open('random.txt', 'a')

# writing to a file
data = "\nThis is some more about it "
f.write(data)

# printing data in file
print(data)

# closeing to a file
f.close()

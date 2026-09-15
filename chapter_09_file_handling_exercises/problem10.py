"""
📚 Topic: Chapter 09 Exercise - Problem 10

Wipe out and clear the entire content of a file using write mode.

💡 Key points:
    1️⃣ Opening a file in `'w'` write mode
    2️⃣ Writing an empty string `""` to truncate the file to 0 bytes
    3️⃣ Confirming empty file state
"""
with open("file1.txt", 'w') as f:
    f.write("")

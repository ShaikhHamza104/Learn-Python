"""
📚 Topic: Chapter 09 Exercise - Problem 1

Read the text file 'poems.txt' and determine whether it contains the word
'twinkle'.

💡 Key points:
    1️⃣ Opening and reading a text file with `open()`
    2️⃣ Case-insensitive substring search using `in`
    3️⃣ Reporting whether the target word is found
"""
# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
with open("poems.txt") as f:
    data = f.read()
    if 'twinkle' in data:
        print("file contain 'Twinkle' ")

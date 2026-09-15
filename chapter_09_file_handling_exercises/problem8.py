"""
📚 Topic: Chapter 09 Exercise - Problem 8

Create an exact copy of a text file 'this.txt' into 'this_copy.txt'.

💡 Key points:
    1️⃣ Reading complete content from the source file
    2️⃣ Writing exact content to the destination file
    3️⃣ Verifying file copying mechanics
"""
with open('this.txt', 'r')as f:
    data = f.read()

with open('this_copy.txt', 'w')as f:
    f.write(data)

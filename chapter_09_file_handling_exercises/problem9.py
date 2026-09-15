"""
📚 Topic: Chapter 09 Exercise - Problem 9

Determine whether two files are completely identical in content.

💡 Key points:
    1️⃣ Reading contents from both files
    2️⃣ Comparing string contents for exact equality
    3️⃣ Reporting match status
"""
# Write a program to find out whether a file is identical & matches the content
# of
# another file.

with open('file1.txt') as f:
    data1 = f.read()

with open('file2.txt') as f:
    data2 = f.read()

if data1 == data2:
    print("Yes this file are identical")
else:
    print("No this file are identical")

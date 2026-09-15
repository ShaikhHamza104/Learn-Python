"""
📚 Topic: Chapter 09 Exercise - Problem 7

Find and report the exact line number where 'python' appears in a log file.

💡 Key points:
    1️⃣ Reading lines sequentially with `f.readline()` or iteration
    2️⃣ Tracking 1-based line numbers
    3️⃣ Identifying matching lines
"""
# Write a program to find out the line number where python is present from ques
# 6.
with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if "Python" in line:
        print(f"Yes python is present on line no {lineno}")
        break
    lineno += 1
else:
    print("Python is not present yet")

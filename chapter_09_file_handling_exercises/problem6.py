"""
📚 Topic: Chapter 09 Exercise - Problem 6

Mine a server log file to determine whether it contains mentions of 'python'.

💡 Key points:
    1️⃣ Reading server log records from disk
    2️⃣ Case-insensitive searching with `.lower()`
    3️⃣ Reporting presence of the query term
"""
# Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt") as f:
    data = f.read()
    if "Python".lower() in data.lower():
        print("Yes files contains 'Python'")
    else:
        print("no files contains 'Python'")

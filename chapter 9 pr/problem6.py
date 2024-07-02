# Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt") as f:
    data=f.read()
    if "Python".lower() in data.lower():
        print("Yes files contains 'Python'")
    else:
        print("no files contains 'Python'")
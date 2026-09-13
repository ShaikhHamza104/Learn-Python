"""
📚 Topic: Constructor Parameters

This script demonstrates constructor parameters using functions and classes.

💡 Key points:
    1️⃣ the basic syntax for constructor parameters
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    constructor parameters affects the result.
"""


class Employee:
    def __init__(self, name, lan, company):
        self.name = name
        self.language = lan
        self.company = company
        print(self.name, self.language, self.company)


emp = Employee("Hamza", "Python", "Microsoft")

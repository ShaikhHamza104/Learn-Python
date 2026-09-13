"""
📚 Topic: Getters and Setters

This script demonstrates getters and setters using while loops, functions
and classes.

💡 Key points:
    1️⃣ the basic syntax for getters and setters
    2️⃣ how while loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    getters and setters affects the result.
"""


class Employee:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @fullName.setter
    def Name(self, name):
        first, last = name.split()
        self.firstName = first
        self.lastName = last


e = Employee("Shaikh", "Hamza")
print(e.fullName)
e.Name = "Khan Rehan"
print(e.fullName)

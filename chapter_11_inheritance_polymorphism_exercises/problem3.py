"""
📚 Topic: Chapter 11 Exercise - Problem 3

This script demonstrates chapter 11 exercise - problem 3 using functions,
classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 11 exercise - problem 3
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 11 exercise - problem 3 affects the result.
"""


class Employee:
    salary = 201
    increment = 22

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e1 = Employee()
e2 = Employee()
e1.increment = 28.8
print(e1.increment)

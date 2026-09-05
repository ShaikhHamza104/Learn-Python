"""
📚 Topic: Class Methods and Functions

This script demonstrates class methods and functions using functions and
classes.

💡 Key points:
    1️⃣ the basic syntax for class methods and functions
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    class methods and functions affects the result.
"""


class Employee:
    salary = 10000  # This is class attribut
    company = "Micosoft"
    language = "Python"

    def getInfo(self):
        print(
            f"The language of Employee is {self.language} and "
            f"company of employee is {self.company}"
        )

    @staticmethod
    def greete():
        print("Good luck")


emp1 = Employee()  # Employee.getInfo(emp1)
emp1.greete()
emp1.getInfo()

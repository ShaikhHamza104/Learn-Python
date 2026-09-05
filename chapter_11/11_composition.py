"""
📚 Topic: Composition vs Inheritance

This script demonstrates composition vs inheritance using for loops, functions
and classes.

💡 Key points:
    1️⃣ the basic syntax for composition vs inheritance
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    composition vs inheritance affects the result.
"""


class Employee:
    def __init__(self) -> None:
        self.name = "Hamza"
        self.qualification = "Diploma pass"
        self.age = 18
        self.work = "Python"
        self.salary = 8000

    def printSalary(self):
        print(f"Name of employee is {self.name} and salary is {self.salary}")


class Bonus:
    def __init__(self):
        self.employee = Employee()

    def getBous(self):
        self.calculate_bous = self.employee.salary * 8.33 / 100
        print(
            f"Name of employee is {self.employee.name} and salary is "
            f"{self.employee.salary} and give bounus is {self.calculate_bous}"
        )


e1 = Bonus()
e1.getBous()

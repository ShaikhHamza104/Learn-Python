"""
📚 Topic: Composition over Inheritance

This script demonstrates composition: building complex objects by combining
other objects rather than inheriting.

💡 Key points:
    1️⃣ "Has-a" relationship (e.g. an Employee *has a* bonus calculator)
    2️⃣ Storing references to component objects as instance attributes
    3️⃣ Providing greater flexibility and loose coupling than inheritance

🧠 Beginner tip:
    Favor composition over inheritance when you want to reuse functionality
    without creating a rigid class hierarchy.
"""


class Employee:
    def __init__(self) -> None:
        self.name = "Hamza"
        self.qualification = "Diploma pass"
        self.age = 18
        self.work = "Python"
        self.salary = 8000

    def print_salary(self):
        print(f"Name of employee is {self.name} and salary is {self.salary}")


class Bonus:
    def __init__(self):
        self.employee = Employee()

    def get_bonus(self):
        self.calculate_bonus = self.employee.salary * 8.33 / 100
        print(
            f"Name of employee is {self.employee.name} and salary is "
            f"{self.employee.salary} and bonus is {self.calculate_bonus}"
        )


e1 = Bonus()
e1.get_bonus()

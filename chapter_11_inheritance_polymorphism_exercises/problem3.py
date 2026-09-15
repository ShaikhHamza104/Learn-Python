"""
📚 Topic: Chapter 11 Exercise - Problem 3

Create an Employee class with salary and increment properties, and implement
getter and setter for salary after increment.

💡 Key points:
    1️⃣ `@property` getter for computed `salary_after_increment`
    2️⃣ `@salary_after_increment.setter` to update the increment percentage
    3️⃣ Clean attribute-like mathematical interface
"""


class Employee:
    salary = 201
    increment = 22

    @property
    def salary_after_increment(self):
        return (self.salary + self.salary * (self.increment / 100))

    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e1 = Employee()
e2 = Employee()
e1.increment = 28.8
print(e1.increment)

"""
📚 Topic: Instance Methods & the `self` Parameter

This script demonstrates defining methods on classes and using the `self`
parameter to access instance data.

💡 Key points:
    1️⃣ The `self` parameter references the specific calling instance
    2️⃣ Calling `obj.method()` automatically passes `obj` as the first argument
    3️⃣ Defining utility static methods with `@staticmethod`

🧠 Beginner tip:
    `self` is not a Python keyword, but a universally followed convention;
    always name the first instance method parameter `self`.
"""


class Employee:
    salary = 10000  # This is class attribute
    company = "Microsoft"
    language = "Python"

    def get_info(self):
        print(
            f"The language of Employee is {self.language} and "
            f"company of employee is {self.company}"
        )

    @staticmethod
    def greet():
        print("Good luck")


emp1 = Employee()  # Employee.get_info(emp1)
emp1.greet()
emp1.get_info()

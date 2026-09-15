"""
📚 Topic: Property Getters and Setters

This script demonstrates defining full getter and setter property pairs to
validate and control attribute modifications.

💡 Key points:
    1️⃣ Defining getter with `@property`
    2️⃣ Defining setter with `@<property_name>.setter`
    3️⃣ Updating underlying state and enforcing business invariants

🧠 Beginner tip:
    Always match the setter function name to the property getter function
    name.
"""


class Employee:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first_name = first
        self.last_name = last


e = Employee("Shaikh", "Hamza")
print(e.full_name)
e.full_name = "Khan Rehan"
print(e.full_name)

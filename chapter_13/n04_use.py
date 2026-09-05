"""
📚 Topic: N04 Use

This script demonstrates n04 use using imports.

💡 Key points:
    1️⃣ the basic syntax for n04 use
    2️⃣ how imports fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    n04 use affects the result.
"""


# Basic import:

from n03_if_name_main import *

# Importing specific functions:
from n03_if_name_main import Employee
from n03_if_name_main import Employee as emp

e2 = Employee("Rahul", "Microsoft")
e2.hello()
e2.printCompany()

# Renaming modules or functions:
s = emp("Sonu", "Google")
s.hello()
s.printCompany()

# from module_name import * (generally discouraged)
emp1 = Employee("Rohi", "Google")
emp1.hello()
emp1.printCompany()

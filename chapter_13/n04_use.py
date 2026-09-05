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

# Importing specific functions:
from n03_if_name_main import Employee
from n03_if_name_main import Employee as emp

e2 = Employee("Rahul", "Microsoft")
e2.hello()
company_info = e2.printCompany
print(company_info)
# Renaming modules or functions:
s = emp("Sonu", "Google")
s.hello()
company_info = s.printCompany
print(company_info)

# from module_name import * (generally discouraged)
emp1 = Employee("Rohi", "Google")
emp1.hello()
company_info = emp1.printCompany
print(company_info)

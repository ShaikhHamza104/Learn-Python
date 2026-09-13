"""
📚 Topic: Mod4 Module Imports

This script demonstrates mod4 module imports using imports.

💡 Key points:
    1️⃣ the basic syntax for mod4 module imports
    2️⃣ how imports fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    mod4 module imports affects the result.
"""

# Importing specific functions:
from mod3_if_name_main import Employee
from mod3_if_name_main import Employee as emp

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

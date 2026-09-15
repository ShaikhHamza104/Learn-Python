"""
📚 Topic: Selective Imports (`from module import ...`)

This script demonstrates importing specific classes and functions directly
into the current namespace.

💡 Key points:
    1️⃣ Selective import: `from module import Item`
    2️⃣ Renaming imports: `from module import Item as RenamedItem`
    3️⃣ Avoiding wildcard imports (`from module import *`) in production

🧠 Beginner tip:
    Wildcard imports pollute the local namespace and obscure where names
    originate, making debugging difficult.
"""


# Importing specific functions:
from mod3_if_name_main import Employee
from mod3_if_name_main import Employee as emp

e2 = Employee("Rahul", "Microsoft")
e2.hello()
company_info = e2.company_info
print(company_info)
# Renaming modules or functions:
s = emp("Sonu", "Google")
s.hello()
company_info = s.company_info
print(company_info)

# from module_name import * (generally discouraged)
emp1 = Employee("Rohi", "Google")
emp1.hello()
company_info = emp1.company_info
print(company_info)

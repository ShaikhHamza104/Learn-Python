# Basic import:

import n03_if_name_main

# Importing specific functions:

from n03_if_name_main import Employee 
e2=Employee("Rahul","Microsoft")
e2.hello()
e2.printCompany()

# Renaming modules or functions:
from n03_if_name_main import Employee as emp
s=emp("Sonu","Google")
s.hello()
s.printCompany()

# from module_name import * (generally discouraged)
from n03_if_name_main import *
emp1=Employee("Rohi","Google")
emp1.hello()
emp1.printCompany()
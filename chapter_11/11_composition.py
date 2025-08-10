class Employee:
    def __init__(self) -> None:
        self.name="Hamza"
        self.qualification="Diploma pass"
        self.age=18
        self.work="Python"
        self.salary=8000
    def printSalary(self):
        print(f"Name of employee is {self.name} and salary is {self.salary}")

class Bonus:
    def __init__(self):
        self.employee=Employee()
        
    def getBous(self):
        self.calculate_bous=self.employee.salary*8.33/100
        print(f"Name of employee is {self.employee.name} and salary is {self.employee.salary} and give bounus is {self.calculate_bous}")
    
e1=Bonus()
e1.getBous()
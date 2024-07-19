class Employee:
    salary=10000 #This is class attribut 
    company="Micosoft"
    language="Python"
    def getInfo(self):
        print(f"The language of Employee is {self.language} and company of employee is {self.company}")  
    @staticmethod
    def greete():
        print("Good luck")
emp1=Employee()  #  Employee.getInfo(emp1) 
emp1.greete()
emp1.getInfo()

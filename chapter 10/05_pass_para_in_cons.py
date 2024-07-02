class Employee:
    def __init__(self,name,lan,company):
        self.name=name
        self.language=lan
        self.company=company
        print(self.name,self.language,self.company)
emp=Employee("Hamza","Python","Microsoft")
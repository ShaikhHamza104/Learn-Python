class Employee:
    company="Microsoft"
    
    @classmethod
    def changeCompany(cls,company):
        cls.company=company


e=Employee()
print(e.company)
e.changeCompany("Gooogle")
print(e.company)
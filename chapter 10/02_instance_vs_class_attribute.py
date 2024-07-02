class Employee:
    salary=10000 #This is class attribut 
    company="Micosoft"
    language="Python"

emp1=Employee()
emp2=Employee()

emp1.name="Hamza" #This is an object/ instance attribut 
print(emp1.name,emp1.company,emp1.language)

emp2.language="Java"
print(emp2.language,emp2.company)
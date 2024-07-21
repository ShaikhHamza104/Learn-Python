class Employee:
    def __init__(self,firstname,lastname):
        self.firstName=firstname
        self.lastName=lastname
    
    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"
    @fullName.setter
    def Name(self,name):
        first,last=name.split()
        self.firstName=first
        self.lastName=last

e=Employee("Shaikh","Hamza")
print(e.fullName)
e.Name="Khan Rehan"
print(e.fullName)
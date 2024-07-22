class Empolyee:
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.company=company

    def show(self):
        print(f"The name of employee is {self.name}.\nAge of employee is {self.age }, and his working in {self.company}")
e1=Empolyee(name="Hamza",age=18,company="Google")
try:
    print(e1.gender)
except AttributeError:
    print(f"This attribute not define in this class ")
e1.show()
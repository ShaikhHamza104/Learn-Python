class Person:
    def __init__(self,name,age,qualification):
        self.name=name
        self.age=age
        self.qualification=qualification
a=Person("Hamza",19,"Diploma Pass")
print(a.__dict__)
print(help(a))
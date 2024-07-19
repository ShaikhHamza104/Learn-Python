class Employee:
    @staticmethod
    def greete():
        print("Welcome")
    def getName(self,name):
        self.name=name
        print(f"Your name is {self.name}")
e1=Employee()
e1.greete()
name=input("Enter your name : ")
e1.getName(name)
class Employee:
    def __init__(self,name,com) -> None:
        self.name=name
        self.company=com

    @staticmethod
    def hello():
        print(f"Hello Empolyee")

    @property
    def printCompany(self):
        return f"Your company name is {self.company}"
        
if __name__ =="__main___":
    e1=Employee("Hamza","Google")
    e1.hello()
    print(e1.printCompany)

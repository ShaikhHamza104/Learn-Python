# 3. Create a class ‘Employee’ and add salary and increment properties to it
class Employee:
    salary=201
    increment=22

    @property
    def salaryAfterIncrement(self):
        return (self.salary+self.salary*(self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=((salary/self.salary)-1)*100

e1=Employee()
e2=Employee()
e1.increment=28.8
print(e1.increment)
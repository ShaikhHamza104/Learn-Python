class A:
    first=0
    def getValueA(self):
        global first
        self.first=int(input("Enter first number "))

# B class inherit A class
class B(A):
    second=0
    def getValueB(self):
        global second
        self.second=int(input("Enter second number "))
    
# C class inherit B class
class C(B): 
    def sum(self):
        return self.first+self.second
    
    def minus(self):
        return self.first-self.second
    
    def mul(self):
        return self.first*self.second
    
    def div(self):
        return self.first/self.second
o=C()
o.getValueA()
o.getValueB()
print("Sum is ",o.sum())
print("Minus is ",o.minus())
print("Multiply is ",o.mul())
print("Devision is ",o.div())

# Creating class A 
class A:
    def methodA(self):
        print("This method belong to Class A")

# Creating class B
class B(A):
    def methodB(self):
        print("This method belong to Class B")

# Creating class B object 
obj=B()

# Calling method for Class A  
obj.methodA()

# Calling method for Class b  
obj.methodB()
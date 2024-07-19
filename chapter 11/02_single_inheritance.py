# Creating class A 
class A:
    name="Class A"
    def methodA(self):
        print("This method belong to Class A")
        print(f"My class name is {self.name}")

# B class inheriting the property ,class attribute from class A
class B(A):
    name="Class B" #Overide class A attribute eg . name 
    def methodB(self):
        print("This method belong to Class B")
        print(f"My class name is {self.name}")

# Creating class B object 
obj=B()

# Calling method for Class A  
obj.methodA()

# Calling method for Class b  
obj.methodB()
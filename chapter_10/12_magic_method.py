class Employee:
    name="Hamza"
    def __init__(self):
        pass

    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"This object belong to Employee class"
    
    def __repr__(self):
        return f"Employee()"
    
    def __call__(self) :
        print("Hi ,I am object of this class")
e=Employee()
print(len(e))
print(str(e))
print(repr(e))
e()
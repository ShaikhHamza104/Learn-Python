# Create a Base Class 
class Base:
    def __init__(self) :
        self._name="Rohan"

# Create a Drived Class 
class Drived(Base):
    def __init__(self):
        super().__init__()
        print("Calling protected member of base class:",self._name) 

        # Modify the protected variable: 
        self._name="Rohi"
        print("Calling modified protected member outside class:",self._name)

# creating a Object for Drived Class .
d=Drived()
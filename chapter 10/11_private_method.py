# Create a Base Class 
class Base:
    def __init__(self) :
        self.__name="Rohan"

# Create a Drived Class 
class Drived(Base):
    def __init__(self):
        super().__init__()
        print("Calling protected member of base class:",self._name) 

        # Modify the protected variable: 
        self.__name="Rohi"
        print("Calling modified protected member outside class:",self._name)

# creating a Object for Base Class .
b=Base()
# It will gernate an Attribute Error:
# print(b.__name)

class MyClass:
    def __init__(self,value):
        self.value=value
        
    # To access to Function as Value 
    @property
    def getValue(self):
        return self.value
o=MyClass(10)
print(o.getValue)
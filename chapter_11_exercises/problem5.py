# 5. Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return f"{self.x+other.x}+{self.y+other.y}"
    def __mul__(self,other):
        return f"{self.x*other.x}+{self.y*other.y}"
    

v1=Vector(1,2)
v2=Vector(3,4)
print(v1+v2)
print(v1*v2)

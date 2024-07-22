# 6. Write __str__() method to print the vector as follows: 7i + 8j +10k
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j +{self.k}"
    def __add__(self,other):
        return f"{self.i+other.i}i + {self.j+other.j}j + {self.k+other.k}k"
    def __mul__(self,other):
        return f"{self.i*other.i}i x {self.j*other.j}j x {self.k*other.k}k"
        
v1=Vector(3,4,5)
v2=Vector(4,4,5)
print(v1+v2)
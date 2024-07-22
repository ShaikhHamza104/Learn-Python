# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"Two D Vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"Two D Vector is {self.i}i + {self.j}j + {self.k}k")
        
t=TwoDVector(12,14)
t.show()
th=ThreeDVector(1,2,13)
th.show()
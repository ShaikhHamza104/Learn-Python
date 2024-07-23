# Create a class Rectangle with methods to calculate the area and perimeter. Use exception handling within the methods to ensure valid dimensions (non-negative values).
class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
        if self.length<=0 or self.width<=0:
            raise ValueError

    def areaOfRectangle(self):
        self.area=self.length*self.width
        print(f"Area of rectangle is {self.area}")
    def perimeterOfRectangle(self):
        self.perimeter=2*(self.length+self.width)
        print(f"perimeter of Rectangle is {self.perimeter}")
try:    
    r=Rectangle(12,2)
    r.areaOfRectangle()
    r.perimeterOfRectangle()
except ValueError:
    print("Please check the paramiter of this constructor")
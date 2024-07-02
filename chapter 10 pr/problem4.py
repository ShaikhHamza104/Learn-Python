# 4. Add a static method in problem 2, to greet the user with hello.
import math 
class Calculator:
    def findSquare(self,n):
        print("{} * {} = {}".format(n,n,n**2))
        
    def findCube(self,n):
        print("{} * {} * {} = {}".format(n,n,n,n**3))

    def findRoot(self,n):
        print(math.sqrt(n))
    
    @staticmethod
    def greete():
        print("Hello ")
user=Calculator()
user.greete()
user.findSquare(n=10)
user.findCube(n=2)
user.findRoot(n=64)
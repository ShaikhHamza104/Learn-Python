# Write a class “Calculator” capable of finding square, cube and square root of a number.
import math 
class Calculator:
    def findSquare(self,n):
        print("{} * {} = {}".format(n,n,n**2))
        
    def findCube(self,n):
        print("{} * {} * {} = {}".format(n,n,n,n**3))

    def findRoot(self,n):
        print(math.sqrt(n))

user=Calculator()
user.findSquare(n=10)
user.findCube(n=2)
user.findRoot(n=64)
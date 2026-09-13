"""
📚 Topic: Problem6

This script demonstrates problem6 using conditions, functions, classes and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem6
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem6 affects the result.
"""


# Create a Rectangle class that calculates area and perimeter. Use exception
# handling to reject negative dimensions.
class Rectangle:
    def __init__(self, l, w):  # noqa: E741
        self.length = l
        self.width = w
        if self.length <= 0 or self.width <= 0:
            raise ValueError

    def areaOfRectangle(self):
        self.area = self.length * self.width
        print(f"Area of rectangle is {self.area}")

    def perimeterOfRectangle(self):
        self.perimeter = 2 * (self.length + self.width)
        print(f"perimeter of Rectangle is {self.perimeter}")


try:
    r = Rectangle(12, 2)
    r.areaOfRectangle()
    r.perimeterOfRectangle()
except ValueError:
    print("Please check the paramiter of this constructor")

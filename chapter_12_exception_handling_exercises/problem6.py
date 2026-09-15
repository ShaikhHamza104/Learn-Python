"""
📚 Topic: Chapter 12 Exercise - Problem 6

Create a Rectangle class that raises `ValueError` for non-positive dimensions.

💡 Key points:
    1️⃣ Validating constructor arguments (`length > 0`, `width > 0`)
    2️⃣ Raising `ValueError` on invalid dimensions
    3️⃣ Calculating area and perimeter safely
"""


# Create a Rectangle class that calculates area and perimeter. Use exception
# handling to reject negative dimensions.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Dimensions must be positive.")

    def area_of_rectangle(self):
        self.area = self.length * self.width
        print(f"Area of rectangle is {self.area}")

    def perimeter_of_rectangle(self):
        self.perimeter = 2 * (self.length + self.width)
        print(f"Perimeter of rectangle is {self.perimeter}")


try:
    r = Rectangle(12, 2)
    r.area_of_rectangle()
    r.perimeter_of_rectangle()
except ValueError:
    print("Please check the parameter of this constructor")

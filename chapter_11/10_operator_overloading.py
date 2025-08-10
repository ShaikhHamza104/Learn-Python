class OperatorOverloading:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return OperatorOverloading(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return OperatorOverloading(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return OperatorOverloading(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return OperatorOverloading(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create instances of the class
v1 = OperatorOverloading(2, 3)
v2 = OperatorOverloading(4, 5)

# Perform operations
add_result = v1 + v2
sub_result = v1 - v2
mul_result = v1 * v2
div_result = v1 / v2

# Print results
print(f"Addition: {add_result}")       # Output: (6, 8)
print(f"Subtraction: {sub_result}")    # Output: (-2, -2)
print(f"Multiplication: {mul_result}") # Output: (8, 15)
print(f"Division: {div_result}")       # Output: (0.5, 0.6)
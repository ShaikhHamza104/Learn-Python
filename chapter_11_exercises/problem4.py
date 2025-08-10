class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __mul__(self, c):
        real_part = self.real * c.real - self.imag * c.imag
        imag_part = self.real * c.imag + self.imag * c.real
        return Complex(real_part, imag_part)

    def __str__(self) -> str:
        return f"{self.real}+{self.imag}i"

# Create instances of Complex
a = Complex(1, 2)
b = Complex(3, 4)

# Print results of addition and multiplication
print(a + b)  # Output: 4+6i
print(a * b)  # Output: -5+10i

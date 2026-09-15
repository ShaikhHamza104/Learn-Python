"""
📚 Topic: Chapter 08 Exercise - Problem 2

Convert Fahrenheit temperatures to Celsius using a custom function.

💡 Key points:
    1️⃣ Applying the conversion formula: `C = 5 * (F - 32) / 9`
    2️⃣ Accepting numerical user input
    3️⃣ Rounding results to two decimal places
"""


# Formula: C = 5 * (F - 32) / 9
def fahrenheit_to_celsius(f):
    return 5 * (f - 32) / 9


f = int(input("Enter temperature in F : "))
print(f"Fahrenheit {f} to Celsius is {round(fahrenheit_to_celsius(f), 2)}")

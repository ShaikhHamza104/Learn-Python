"""
📚 Topic: Chapter 08 Exercise - Problem 6

Write a python function to convert inches into centimeters.

💡 Key points:
    1️⃣ Conversion factor: 1 inch = 2.54 cm
    2️⃣ Accepting numeric input from user
    3️⃣ Returning the converted centimeter value
"""


def inches_to_cms(inches):
    return inches * 2.54


inches_val = int(input("Enter inches : "))
print(inches_to_cms(inches=inches_val))

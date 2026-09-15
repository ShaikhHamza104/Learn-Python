"""
📚 Topic: Chapter 08 Exercise - Problem 8

Print the multiplication table of a given number using a custom function.

💡 Key points:
    1️⃣ Encapsulating loop logic inside a function
    2️⃣ Iterating through 1 to 10
    3️⃣ Formatting table rows with f-strings
"""


def multiplication(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


num = int(input("Enter a number "))
multiplication(num)

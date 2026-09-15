"""
📚 Topic: Chapter 12 Exercise - Problem 1

Prompt for user input and handle invalid integer inputs using `ValueError`.

💡 Key points:
    1️⃣ Converting user string input to `int` inside `try`
    2️⃣ Catching `ValueError` when non-numeric strings are entered
    3️⃣ Displaying helpful validation feedback
"""


# 1. Write a program that takes integer input and raises ValueError
# if the input is not an integer.
def input_as_integer():
    try:
        int(input("Enter any number "))
    except ValueError as e:
        print(e)


input_as_integer()

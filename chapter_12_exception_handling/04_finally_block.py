"""
📚 Topic: 04 Finally Block

This script demonstrates 04 finally block using user input, for loops,
conditions and exception handling.

💡 Key points:
    1️⃣ the basic syntax for 04 finally block
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    04 finally block affects the result.
"""


def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b


opration = {
    "+": add,
    "-": sub,
    "x": mul,
    "/": div
}

try:
    a = int(input("Enter first number: "))

    for oprator in opration:
        print(oprator)
    o = input("Enter oprator ")
    b = int(input("Enter second number: "))


except ValueError:
    print("Please check your inputs ")

except KeyError:
    print("Please enter a valid oprator ")

else:
    if o == "+":
        print(f"Addition of {a} and {b}", add(a, b))

    elif o == "-":
        print(f"Subtraction of {a} and {b}", sub(a, b))

    elif o == "*":
        print(f"Multiplication of {a} and {b}", mul(a, b))

    elif o == "/":
        print(f"Division of {a} and {b}", div(a, b))

finally:
    print("Thanks for using calculator")

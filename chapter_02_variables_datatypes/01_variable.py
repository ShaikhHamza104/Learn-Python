"""
📚 Topic: Variables & Memory Assignment

This script demonstrates assigning various Python objects to named variables,
inspecting them, and understanding how variables act as labeled references
to values in computer memory.

💡 Key points:
    1️⃣ Assigning primitive literals (integers, floats, strings) to variables
    2️⃣ Reassigning variables dynamically without explicit type declarations
    3️⃣ Printing variable contents using modern f-strings

🧠 Beginner tip:
    In Python, you do not declare variable types beforehand; Python infers
    the type at runtime based on the value assigned to the variable.
"""


def main():
    """
    This function provides examples of variable assignment.
    """
    # Direct assignment
    integer_variable = 10
    float_variable = 10.10
    string_variable = "Hello, Python!"

    print(f"Integer variable: {integer_variable}")
    print(f"Float variable: {float_variable}")
    print(f"String variable: {string_variable}")

    # Assignment using constructors
    integer_variable_2 = 20
    float_variable_2 = 56.90
    string_variable_2 = "Python"

    print(f"Integer variable 2: {integer_variable_2}")
    print(f"Float variable 2: {float_variable_2}")
    print(f"String variable 2: {string_variable_2}")


if __name__ == "__main__":
    main()

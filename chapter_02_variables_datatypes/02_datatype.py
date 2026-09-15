"""
📚 Topic: Fundamental Python Data Types

This script explores Python's primary built-in data types (integers, floats,
strings, booleans, and NoneType), verifying their types at runtime using the
built-in `type()` function.

💡 Key points:
    1️⃣ Numeric types: integers (`int`) and floating-point floats (`float`)
    2️⃣ Text representations: strings (`str`) enclosed in quotes
    3️⃣ Logic and absence: truth flags (`bool`) and empty markers (`NoneType`)

🧠 Beginner tip:
    `None` is not zero or an empty string; it is a unique singleton in Python
    representing the intentional absence of any value.
"""


def main():
    """
    This function provides examples of basic data types.
    """
    # Integer
    integer_variable = 10
    print(f"'{integer_variable}' is of type {type(integer_variable)}")

    # Float
    float_variable = 7.5
    print(f"'{float_variable}' is of type {type(float_variable)}")

    # String
    string_variable = "Hamza"
    print(f"'{string_variable}' is of type {type(string_variable)}")

    # Boolean
    boolean_variable = True
    print(f"'{boolean_variable}' is of type {type(boolean_variable)}")

    # NoneType
    none_variable = None
    print(f"'{none_variable}' is of type {type(none_variable)}")


if __name__ == "__main__":
    main()

"""
📚 Topic: Datatype

This script demonstrates datatype using functions and conditions.

💡 Key points:
    1️⃣ the basic syntax for datatype
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    datatype affects the result.
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

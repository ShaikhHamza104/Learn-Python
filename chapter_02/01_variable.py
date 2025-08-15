#!/usr/bin/env python
"""
This script demonstrates variable assignment in Python.
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
    integer_variable_2 = int(20)
    float_variable_2 = float(56.90)
    string_variable_2 = str("Python")

    print(f"Integer variable 2: {integer_variable_2}")
    print(f"Float variable 2: {float_variable_2}")
    print(f"String variable 2: {string_variable_2}")

if __name__ == "__main__":
    main()

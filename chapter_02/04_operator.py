"""
📚 Topic: Operator

This script demonstrates operator using functions and conditions.

💡 Key points:
    1️⃣ the basic syntax for operator
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    operator affects the result.
"""


def arithmetic_operators():
    """Demonstrates arithmetic operators."""
    print("--- Arithmetic Operators ---")
    a = 10
    b = 5
    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a % b = {a % b}")
    print(f"a ** b = {a**b}")
    print(f"a // b = {a // b}")
    print("-" * 20)


def assignment_operators():
    """Demonstrates assignment operators."""
    print("--- Assignment Operators ---")
    a = 10
    print(f"a = {a}")
    a += 5
    print(f"a += 5 -> a = {a}")
    a -= 5
    print(f"a -= 5 -> a = {a}")
    a *= 5
    print(f"a *= 5 -> a = {a}")
    a /= 5
    print(f"a /= 5 -> a = {a}")
    print("-" * 20)


def comparison_operators():
    """Demonstrates comparison operators."""
    print("--- Comparison Operators ---")
    a = 10
    b = 5
    print(f"a = {a}, b = {b}")
    print(f"a == b -> {a == b}")
    print(f"a != b -> {a != b}")
    print(f"a > b -> {a > b}")
    print(f"a < b -> {a < b}")
    print(f"a >= b -> {a >= b}")
    print(f"a <= b -> {a <= b}")
    print("-" * 20)


def logical_operators():
    """Demonstrates logical operators."""
    print("--- Logical Operators ---")
    a = True
    b = False
    print(f"a = {a}, b = {b}")
    print(f"a and b -> {a and b}")
    print(f"a or b -> {a or b}")
    print(f"not a -> {not a}")
    print("-" * 20)


def membership_operators():
    """Demonstrates membership operators."""
    print("--- Membership Operators ---")
    my_list = [1, 2, 3, 4, 5]
    print(f"my_list = {my_list}")
    print(f"3 in my_list -> {3 in my_list}")
    print(f"6 in my_list -> {6 in my_list}")
    print(f"3 not in my_list -> {3 not in my_list}")
    print(f"6 not in my_list -> {6 not in my_list}")
    print("-" * 20)


def identity_operators():
    """Demonstrates identity operators."""
    print("--- Identity Operators ---")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"a = {a}, b = {b}, c = a")
    print(f"a is b -> {a is b}")
    print(f"a is not b -> {a is not b}")
    print(f"a is c -> {a is c}")
    print("-" * 20)


def bitwise_operators():
    """Demonstrates bitwise operators."""
    print("--- Bitwise Operators ---")
    a = 12  # binary: 1100
    b = 10  # binary: 1010
    print(f"a = {a} (binary: {bin(a)}), b = {b} (binary: {bin(b)})")
    print(f"a & b -> {a & b} (binary: {bin(a & b)})")
    print(f"a | b -> {a | b} (binary: {bin(a | b)})")
    print(f"a ^ b -> {a ^ b} (binary: {bin(a ^ b)})")
    print(f"~a -> {~a} (binary: {bin(~a)})")
    print(f"a << 2 -> {a << 2} (binary: {bin(a << 2)})")
    print(f"a >> 2 -> {a >> 2} (binary: {bin(a >> 2)})")
    print("-" * 20)


def main():
    """
    This function calls all the operator demonstration functions.
    """
    arithmetic_operators()
    assignment_operators()
    comparison_operators()
    logical_operators()
    membership_operators()
    identity_operators()
    bitwise_operators()


if __name__ == "__main__":
    main()

"""
📚 Topic: First Steps - Running Python & The Main Execution Pattern

This script introduces Python's foundational print output and the standard
`if __name__ == '__main__':` execution guard. Writing programs inside a
dedicated entrypoint function is a software engineering best practice that
allows code to be imported as a module without running automatically.

💡 Key points:
    1️⃣ Using `print()` to output text to the standard console
    2️⃣ Defining a top-level `main()` function to organize program entry
    3️⃣ Protecting execution with `if __name__ == '__main__':`

🧠 Beginner tip:
    Whenever you execute a Python file directly, Python sets its internal
    variable `__name__` to '__main__', triggering the execution block.
"""


def main():
    """Prints "Hello, world!" to the console."""
    print("Hello, world!")


if __name__ == "__main__":
    main()

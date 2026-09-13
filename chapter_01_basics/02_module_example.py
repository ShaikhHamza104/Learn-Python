"""
📚 Topic: Modules in Python

This script demonstrates modules in python using functions, conditions and
imports.

💡 Key points:
    1️⃣ the basic syntax for modules in python
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    modules in python affects the result.
"""


import pyjokes


def print_joke():
    """
    Gets a random joke from the pyjokes library and prints it.
    """
    joke_text = pyjokes.get_joke()
    print(joke_text)


if __name__ == "__main__":
    print_joke()

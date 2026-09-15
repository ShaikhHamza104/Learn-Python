"""
📚 Topic: Third-Party Modules & Libraries

This script demonstrates how to import and utilize third-party Python modules
installed from PyPI. Reusable packages (like `pyjokes`) expand Python's
built-in capabilities without requiring you to reinvent the wheel.

💡 Key points:
    1️⃣ Importing external packages using the `import` statement
    2️⃣ Calling library functions using dot notation (`module.function()`)
    3️⃣ Structuring calls inside clean entrypoint functions

🧠 Beginner tip:
    Before importing any third-party library, remember to install it inside
    your active virtual environment using `pip install <package_name>`.
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

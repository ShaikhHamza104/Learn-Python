"""
📚 Topic: Python Packages and `__init__.py`

This script explains how directories containing `__init__.py` files form
hierarchical Python packages.

💡 Key points:
    1️⃣ A package is a directory containing an `__init__.py` file
    2️⃣ Organizing related modules into structured sub-namespaces
    3️⃣ Exposing public package APIs via `__init__.py`

🧠 Beginner tip:
    In Python 3.3+, namespace packages can exist without `__init__.py`, but
    regular packages still use `__init__.py` for initialization and exports.
"""


# ----------------
# my_package/
# ├── __init__.py      <- this file makes the folder a "package"
# ├── math_utils.py
# └── string_utils.py
#
# Without __init__.py, Python just sees a normal folder - not a package
# (Note: since Python 3.3 this isn't STRICTLY required anymore, but every
#  real project still includes it - it's considered best practice)


# ---------------------------------------------------
# 📝 2. What goes inside __init__.py?
# ---------------------------------------------------
# It can literally be EMPTY - that alone is enough to turn a folder
# into a package. But most of the time, people use it to control what
# gets imported when someone does `import my_package`

# Example __init__.py content:
"""
📚 Topic: Python packages and __init__.py

This script demonstrates Python packages and __init__.py using imports.

💡 Key points:
    1️⃣ the basic syntax for python packages and __init__.py
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Read the examples, then create a small package with your own modules.
"""
# This means someone can now do:
#   from my_package import add
# instead of the longer:
#   from my_package.math_utils import add


# ---------------------------------------------------
# 🧑‍💻 3. A tiny working example
# ---------------------------------------------------
# Imagine this folder structure sitting next to this file:
#
# calculator_package/
# ├── __init__.py
# └── operations.py
#
# operations.py would contain:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""
#
# __init__.py would contain:
"""
from .operations import add, subtract
"""
#
# Then anywhere else in your project you could write:
"""
from calculator_package import add, subtract

print(add(5, 3))       # 8
print(subtract(5, 3))  # 2
"""


# ---------------------------------------------------
# 🆚 import module vs import package
# ---------------------------------------------------
# import a single module:      import mod1_intro_module
# import from a package:       from calculator_package import add
# import the whole package:    import calculator_package
#                               calculator_package.add(2, 3)


# ---------------------------------------------------
# 🌍 4. Real world example you already use
# ---------------------------------------------------
# "numpy" is a PACKAGE, not a single file - that's why you can do both:
#   import numpy as np
#   np.array([1, 2, 3])
# ...and also:
#   from numpy import array
#   array([1, 2, 3])
# Both work because of how numpy's __init__.py is written.


# ---------------------------------------------------
# 💡 Why does this matter for Data Science?
# ---------------------------------------------------
# Once your projects grow past a few files, you'll want to group related
# code together - e.g. a "data_cleaning" package, a "visualization"
# package. This is exactly how libraries like pandas and numpy are
# structured internally.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Forgetting the dot before the module name inside __init__.py
# Correct:   from .operations import add     (relative import - dot means
#            "look inside THIS same package")
# Wrong:     from operations import add      (Python looks for a
#            top-level module called operations and won't find it)

# 🐍 Chapter 13 — Modules & Packages: Organizing Larger Codebases 📦

Welcome to Chapter 13! As your Python applications grow beyond single files, you need a clean way to organize, structure, and share code. **Modules** (single `.py` files) and **Packages** (directories containing modules and an `__init__.py`) form the backbone of Python's modular architecture.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `mod1_intro_module.py` | Creating a Module | Defining functions in a standalone `.py` file |
| 02 | `mod2_module_use.py` | Using Your Module | `import mod1_intro_module` |
| 03 | `mod3_if_name_main.py` | `if __name__ == '__main__':` | Preventing unwanted code execution on import |
| 04 | `mod4_module_imports.py` | Import Techniques | `import`, `from ... import`, `as` aliases |
| 05 | `mod5_package_init.py` | Packages & `__init__.py` | Converting folders into Python packages |
| 06 | `mod6_use_exam.py` | Package Practice | Importing modules from package directories (`Exam/`) |

---

## 📄 1. What is a Module? (`mod1_intro_module.py`, `mod2_module_use.py`)

A **module** is simply any Python file ending in `.py`. Any functions, classes, or variables defined inside it can be imported into another script:

```python
# In mod1_intro_module.py
def greet_user(name):
    return f"Welcome back, {name}!"

PI_CONSTANT = 3.14159
```

```python
# In mod2_module_use.py
import mod1_intro_module as my_mod

print(my_mod.greet_user("Hamza"))
print("Value of PI:", my_mod.PI_CONSTANT)
```

---

## 🚦 2. The `if __name__ == '__main__':` Guard (`mod3_if_name_main.py`)

When Python runs a file directly, it sets the special variable `__name__` to `"__main__"`. When imported as a module, `__name__` is set to the module's actual file name.

```python
def calculate_area(radius):
    return 3.14159 * radius ** 2

# This block ONLY runs when this script is executed directly:
if __name__ == "__main__":
    print("Running tests directly...")
    print("Area of circle (r=5):", calculate_area(5))
```

> [!TIP]
> Always place code that executes actions (prints, tests, user prompts) inside `if __name__ == "__main__":` so other scripts can safely import your functions without triggering unwanted side effects.

---

## 📥 3. Import Styles & Best Practices (`mod4_module_imports.py`)

```python
# 1. Standard module import
import math
print(math.sqrt(16))

# 2. Specific function imports
from math import sqrt, pi
print(sqrt(25))

# 3. Aliasing for convenience or collision prevention
import datetime as dt
print(dt.date.today())

# ❌ BAD PRACTICE: Wildcard imports
# from math import *  # Pollutes namespace and makes debugging difficult!
```

---

## 📦 4. Packages and `__init__.py` (`mod5_package_init.py`, `mod6_use_exam.py`)

A **package** is a directory that contains multiple Python modules and an `__init__.py` file:

```text
my_package/
├── __init__.py      # Package initializer
├── math_tools.py    # Submodule 1
└── string_tools.py  # Submodule 2
```

```python
# Importing from a package
from my_package.math_tools import add_numbers
```

---

## ⏭️ What's Next?
Now learn how to interact with your operating system, files, and modern path objects in **[Chapter 14 — OS Module & Pathlib](../chapter_14/README.md)**!

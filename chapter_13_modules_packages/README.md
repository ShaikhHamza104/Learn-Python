# 📚 Topic: Modules & Packages

As software projects grow, keeping all code in a single file becomes unmaintainable. Python solves this through **modules** (individual `.py` files) and **packages** (directories containing an `__init__.py` file and multiple modules). Modular code enables reusability, clean namespaces, and separation of concerns across large applications.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `mod1_intro_module.py` | Creating a standalone module defining a reusable `Calculator` class |
| `mod2_module_use.py` | Importing a module using `import mod1_intro_module` and invoking its methods |
| `mod3_if_name_main.py` | Protecting execution blocks using the `if __name__ == "__main__":` boilerplate |
| `mod4_module_imports.py` | Importing specific classes with `from ... import`, using aliases with `as`, and namespace pollution |
| `mod5_package_init.py` | Converting directories into packages using `__init__.py`, relative imports, and comparison with libraries like NumPy |
| `mod6_use_exam.py` | Importing and consuming multiple submodules (`avg.py`, `theroy.py`) from the `Exam/` package |
| `Exam/` | A multi-module package containing `__init__.py`, `avg.py`, `ptt1.py`, `ptt2.py`, and `theroy.py` |

---

## 💡 Key points

1. **Creating a Reusable Module (`mod1_intro_module.py`)**: Any standard `.py` file containing classes, functions, or constants acts as a module that other scripts can import and reuse.
2. **Importing Modules (`mod2_module_use.py`)**: Use `import mod1_intro_module` to access members via the module namespace (e.g., `mod1_intro_module.Calculator(a, b)`), keeping naming collisions isolated.
3. **The `__name__ == "__main__"` Guard (`mod3_if_name_main.py`)**: When a script is executed directly, Python sets `__name__` to `"__main__"`. Wrapping runnable logic in this check ensures classes and functions can be imported into other files without triggering unintended execution or side effects.
4. **Selective Imports and Aliasing (`mod4_module_imports.py`)**: Use `from module import Symbol` to bring specific identifiers directly into scope, and `as alias` (such as `import Employee as emp`) for cleaner naming or avoiding identifier collisions. Avoid `from module import *` because it pollutes namespaces and hides source origins.
5. **Packages and `__init__.py` (`mod5_package_init.py`)**: A directory with an `__init__.py` file is recognized as a package. The `__init__.py` file initializes the package and can expose key functions via relative imports (e.g., `from .operations import add`) so callers can import directly from the top package.
6. **Relative Imports Inside Packages (`Exam/avg.py`)**: Submodules within the same package use explicit relative imports (such as `from . import ptt1, ptt2`) to reference sibling modules safely regardless of where the root script is executed.
7. **Multi-Module Orchestration (`mod6_use_exam.py`)**: Applications can import submodules hierarchically (such as `import Exam.avg` and `import Exam.theroy`) and combine calculations across modular components.

---

## 🧠 Beginner tip

When structuring your own package, always use relative imports with a leading dot (e.g., `from .operations import add`) inside your package submodules or `__init__.py`. Omitting the dot (e.g., `from operations import add`) instructs Python to search your global `sys.path` rather than the current package directory, which leads to `ModuleNotFoundError` when your project is executed from different working directories.

---

## 📊 Where this is used in Data Science

- **Custom Feature Engineering Libraries**: Production ML codebases organize data cleaners, custom scikit-learn transformers, and domain metric functions into internal packages (e.g., `features/`, `models/`, `evaluation/`) rather than copy-pasting code into dozens of Jupyter notebooks.
- **Library Internals (NumPy, Pandas, PyTorch)**: Major data science libraries are organized as packages. When you type `import numpy as np` or `from sklearn.ensemble import RandomForestClassifier`, Python resolves submodules through package `__init__.py` definitions.
- **Model Training vs. Inference Separation**: ETL workflows, model training scripts, and real-time prediction servers import shared data validation schemas and preprocessing modules from a single authoritative internal package.

---

## 🛠️ Code Examples

### Defining and Importing a Module
```python
# In math_tools.py
def multiply(x, y):
    return x * y

# In main.py
import math_tools
print(math_tools.multiply(6, 7))
```

### The `if __name__ == "__main__":` Pattern
```python
def process_data(records):
    return [r.strip().lower() for r in records]

if __name__ == "__main__":
    # Runs only when directly executed (e.g. python script.py)
    # Ignored when imported into another script
    test_data = ["  Alpha ", "BETA  "]
    print("Self-test result:", process_data(test_data))
```

### Package Structure and Relative Imports
```python
# Project layout:
# analytics/
# ├── __init__.py
# ├── metrics.py
# └── transforms.py

# Inside analytics/__init__.py:
from .metrics import calculate_accuracy
from .transforms import normalize_features

# Caller usage:
from analytics import calculate_accuracy, normalize_features
```

---

## ⏭️ What's Next

Discover how to navigate directories, manage filesystem paths, and work with modern cross-platform path objects in **[Chapter 14 — OS Module & Pathlib](../chapter_14_os_pathlib/README.md)**!

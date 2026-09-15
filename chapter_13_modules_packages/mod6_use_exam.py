"""
📚 Topic: Using Submodules within a Package

This script demonstrates importing and combining functionality from package
submodules.

💡 Key points:
    1️⃣ Importing submodules from a local package hierarchy
    2️⃣ Calling package functions to aggregate results
    3️⃣ Package directory layout and relative imports

🧠 Beginner tip:
    Ensure the parent directory is on `sys.path` when running scripts that
    import sibling packages.
"""


import Exam
import Exam.avg
import Exam.theory

print(Exam.avg.cal_avg() + Exam.theory.get_theory())

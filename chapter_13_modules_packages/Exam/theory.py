"""
📚 Topic: Exam Package - Theory Test Submodule

This module handles recording and retrieving theory test scores.

💡 Key points:
    1️⃣ Encapsulating theory test score collection
    2️⃣ Returning validated numerical marks
    3️⃣ Integrating into total exam grade calculations
"""


theory = 0


def get_theory():
    global theory
    theory = int(input("Enter your theory marks "))
    return theory


if __name__ == "__main__":
    pass

"""
📚 Topic: Exam Package - Average Calculation Submodule

This module computes average marks across practical test submodules.

💡 Key points:
    1️⃣ Relative import of sibling modules (`from . import ptt1, ptt2`)
    2️⃣ Calculating aggregate averages
    3️⃣ Modular separation of mathematical logic
"""


from . import ptt1, ptt2


def cal_avg():
    return (ptt1.get_ptt1() + ptt2.get_ptt2()) / 2


if __name__ == "__main__":
    pass

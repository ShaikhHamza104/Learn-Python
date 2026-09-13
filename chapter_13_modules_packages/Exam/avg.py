"""
📚 Topic: Avg

This script demonstrates avg using conditions, functions and imports.

💡 Key points:
    1️⃣ the basic syntax for avg
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    avg affects the result.
"""


from . import ptt1, ptt2


def cal_avg():
    return (ptt1.getPtt1() + ptt2.getPtt2()) / 2


if __name__ == "__main__":
    pass

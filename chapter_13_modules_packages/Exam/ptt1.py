"""
📚 Topic: Exam Package - Practical Test 1 Submodule

This module handles recording and retrieving Practical Test 1 marks.

💡 Key points:
    1️⃣ Encapsulating test score retrieval
    2️⃣ Converting input to numeric marks
    3️⃣ Exposing test data to aggregator modules
"""


ptt1 = 0


def get_ptt1():
    global ptt1
    ptt1 = int(input("Enter ppt1 mark "))
    return ptt1


if __name__ == "__main__":
    pass

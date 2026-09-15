"""
📚 Topic: Exam Package - Practical Test 2 Submodule

This module handles recording and retrieving Practical Test 2 marks.

💡 Key points:
    1️⃣ Encapsulating test score retrieval for second practical exam
    2️⃣ Standardized retrieval function
    3️⃣ Sibling submodule in the Exam package
"""


ptt2 = 0


def get_ptt2():
    global ptt2
    ptt2 = int(input("Enter ppt2 mark "))
    return ptt2


if __name__ == "__main__":
    pass

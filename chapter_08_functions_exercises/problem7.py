"""
📚 Topic: Chapter 08 Exercise - Problem 7

This script demonstrates chapter 08 exercise - problem 7 using for loops,
conditions, functions and classes.

💡 Key points:
    1️⃣ the basic syntax for chapter 08 exercise - problem 7
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 08 exercise - problem 7 affects the result.
"""


# . Write a python function to remove a given word from a list and strip it at
# the same time


def rem(l, word):  # noqa: E741
    n = []
    for item in l:  # noqa: E741
        if not (item == word):
            n.append(item.strip(word))
    return n


l = ["Harry", "Rohan", "Roshi", "an"]  # noqa: E741
print(rem(l, "an"))

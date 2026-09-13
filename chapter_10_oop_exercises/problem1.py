"""
📚 Topic: Chapter 10 Exercise - Problem 1

This script demonstrates chapter 10 exercise - problem 1 using for loops,
functions, classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 10 exercise - problem 1
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 10 exercise - problem 1 affects the result.
"""


# . Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class Programmer:
    comany = "Microsoft"  # class attribute
    l = ["harry", "Rehan", "Aman"]  # noqa: E741

    def detailInfo(self):
        for name in self.l:
            print(
                "The name of employee is "
                + name.capitalize()
                + " and capany is "
                + self.comany
            )


obj = Programmer()
obj.detailInfo()

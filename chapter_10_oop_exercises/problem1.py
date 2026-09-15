"""
📚 Topic: Chapter 10 Exercise - Problem 1

Create a Programmer class for storing information about programmers working
at Microsoft.

💡 Key points:
    1️⃣ Defining class-level company affiliation
    2️⃣ Initializing instance-level programmer lists safely
    3️⃣ Iterating and displaying formatted employee details
"""


# . Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class Programmer:
    company = "Microsoft"  # class attribute

    def __init__(self, programmers=None):
        self.programmers = (
            programmers if programmers is not None
            else ["harry", "Rehan", "Aman"]
        )

    def detail_info(self):
        for name in self.programmers:
            print(
                "The name of employee is "
                + name.capitalize()
                + " and company is "
                + self.company
            )


obj = Programmer()
obj.detail_info()

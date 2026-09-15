"""
📚 Topic: Chapter 11 Exercise - Problem 1

Create a 2D vector class and inherit from it to create a 3D vector class.

💡 Key points:
    1️⃣ Defining 2D vector with `i` and `j` components
    2️⃣ Extending via inheritance to 3D vector with `k` component
    3️⃣ Overriding display method to represent 3D vectors
"""


class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"Two D Vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"Three D Vector is {self.i}i + {self.j}j + {self.k}k")


t = TwoDVector(12, 14)
t.show()
th = ThreeDVector(1, 2, 13)
th.show()

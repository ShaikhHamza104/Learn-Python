"""
📚 Topic: Abstract Base Classes (ABC)

This script demonstrates abstract base classes (abc) using for loops,
functions, classes and imports.

💡 Key points:
    1️⃣ the basic syntax for abstract base classes (abc)
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    abstract base classes (abc) affects the result.
"""


from abc import ABC, abstractmethod


class Ploygon(ABC):

    @abstractmethod
    def side(self):
        pass


class Triangle(Ploygon):

    def side(self):
        print("I have 3 side ")


class Square(Ploygon):

    def side(self):
        print("I have 4 side ")


class Hexagon(Ploygon):

    def side(self):
        print("I have 6 side ")


ot = Triangle()
ot.side()

os = Square()
os.side()

oh = Hexagon()
oh.side()

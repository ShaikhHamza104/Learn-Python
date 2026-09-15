"""
📚 Topic: Abstract Base Classes (`abc.ABC`)

This script demonstrates defining formal interfaces using `abc.ABC` and the
`@abstractmethod` decorator.

💡 Key points:
    1️⃣ Inheriting from `abc.ABC` defines an abstract base class
    2️⃣ Marking methods with `@abstractmethod` forces child implementation
    3️⃣ Instantiating incomplete abstract classes raises `TypeError`

🧠 Beginner tip:
    Use abstract base classes to define strict API contracts across multiple
    subclasses.
"""


from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def side(self):
        pass


class Triangle(Polygon):

    def side(self):
        print("I have 3 side ")


class Square(Polygon):

    def side(self):
        print("I have 4 side ")


class Hexagon(Polygon):

    def side(self):
        print("I have 6 side ")


ot = Triangle()
ot.side()

sq = Square()
sq.side()

oh = Hexagon()
oh.side()

from abc import ABC,abstractmethod

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
ot=Triangle()
ot.side()

os=Square()
os.side()

oh=Hexagon()
oh.side()
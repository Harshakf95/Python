from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")
class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")
class Ractangle(Polygon):
    def noofsides(self):
        print("I have 4 sides")
T=Triangle()
T.noofsides()

P=Pentagon()
P.noofsides()

H=Hexagon()
H.noofsides()

R=Ractangle()
R.noofsides()
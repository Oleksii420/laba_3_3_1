from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
from Circle import Circle
from Parallelogram import Parallelogram
from TriangularPyramid import TriangularPyramid
from TriangularPrism import TriangularPrism
from RectangularParallelepiped import RectangularParallelepiped
from QuadrangularPyramid import QuadrangularPyramid
from Cone import Cone
from Ball import Ball
class FigureReader:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        figures = []
        classes = {"Triangle": Triangle, "Rectangle": Rectangle, "Trapeze": Trapeze, "Circle": Circle,
                   "Parallelogram": Parallelogram, "TriangularPyramid": TriangularPyramid, "TriangularPrism": TriangularPrism,
                   "RectangularParallelepiped": RectangularParallelepiped, "QuadrangularPyramid": QuadrangularPyramid,
                   "Cone": Cone, "Ball": Ball}
        with open(self.file_name, "rt") as f:
            for line in f:
                try:
                    data = line.split()
                    figure = data[0]
                    numbers = [float(el) for el in data[1:]]
                    figures.append(classes[figure](*numbers))
                except (AssertionError, KeyError):
                    pass
        return figures
if __name__ == "__main__":
    print(FigureReader("input01.txt"))
    print(FigureReader("input02.txt"))
    print(FigureReader("input03.txt"))
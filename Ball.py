from math import pi
from Figure import Figure

class Ball(Figure):
    def __init__(self, r):
        assert r > 0
        self.r = r
        self.roundedPi = round(pi, 5)

    def volume(self):
        result = (4/3) * pi * self.r ** 3
        return result

    def height(self):
        return self.r * 2

    def squareSurface(self):
        result = 4 * pi * self.r ** 2
        return result

    def squareBase(self):
        return self.squareSurface()

    def perimetr(self):
        result = (4/3) * pi * self.r ** 3
        return result


    def dimention(self):
        return 3

    def __str__(self) -> str:
        return f"Ball: r={self.r}"
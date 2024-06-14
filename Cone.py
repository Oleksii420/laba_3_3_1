from math import pi
from Circle import Circle

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        # assert r > 0 and h > 0
        self.h = h
        self.roundedPi = round(pi, 5)

    def squareBase(self):
        return super().volume()

    def height(self):
        return self.h

    def squareSurface(self):
        l = (self.r ** 2 + self.h ** 2) ** 0.5
        return self.roundedPi * l * self.r

    def volume(self):
        result = 1/3 * self.roundedPi * (self.r ** 2) * self.h
        return result

    def __str__(self) -> str:
        return f"Cone: r={self.r} h={self.h}"
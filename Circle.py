from math import pi
from Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        assert r > 0
        self.r = r
        self.roundedPi = round(pi, 5)


    def perimetr(self):
        result = 2 * self.roundedPi * self.r
        return result

    def square(self):
        result = self.roundedPi * self.r ** 2
        return result

    def volume(self):
        return self.square()

    def dimention(self):
        return 2

    def __str__(self) -> str:
        return f"Circle: r={self.r}"
from Triangle import Triangle

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        # self.a = a #сторона
        self.h = h #висота

    def dimention(self):
        return 3

    def volume(self):
        return (1/3) * super().volume() * self.h

    def height(self):
        return self.h

    def squareBase(self):
        return super().volume()

    def squareSurface(self):
        r = (((3)**0.5)/6) * self.a
        ap = ((self.h)**2 * (r)**2)**0.5
        result = (3/2) * self.a * self.ap
        return result

    def area(self):
        rebro = ((self.a ** 2 + self.h ** 2) ** 0.5)
        pivper1 = rebro * 2 + self.a
        sq1 = ((pivper1 * (pivper1 - rebro) * (pivper1 - rebro) * (pivper1 - self.a)) ** 0.5)
        sq2 = ((self.a ** 2) * (3 ** 0.5)) / 4
        return sq1 * 3 + sq2

    def __str__(self) -> str:
        return f"Triangularpyramid: a={self.a} h={self.h}"


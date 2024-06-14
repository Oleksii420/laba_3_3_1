from Rectangle import Rectangle

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3

    def volume(self):
        return super().volume() * self.h * (1/3)

    def squareBase(self):
        return super().volume()

    def height(self):
        return self.h


    def squareSurface(self):
        halfDiag = (self.a**2 + self.b**2)**0.5 / 2
        edge = (halfDiag**2 + self.h**2)**0.5
        halfPerimeter1 = (edge * 2 + self.a)/2
        halfPerimeter2 = (edge * 2 + self.b)/2
        tr1 = (halfPerimeter1 * (halfPerimeter1 - self.a) * (halfPerimeter1 - edge) * (halfPerimeter1 - edge)) ** 0.5
        tr2 = (halfPerimeter2 * (halfPerimeter2 - self.a) * (halfPerimeter2 - edge) * (halfPerimeter2 - edge)) ** 0.5
        return 2 * tr1 + 2 * tr2




    def __str__(self) -> str:
        return f"QuadrangularPyramid: a={self.a} b={self.b} h={self.h}"
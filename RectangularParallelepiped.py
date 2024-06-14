from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3

    def volume(self):
        return self.a * self.b * self.c

    def height(self):
        return self.c

    def squareBase(self):
        return super().volume()


    def squareSurface(self):
        return self.h * self.a * 2 + self.h * self.b * 2



    def __str__(self) -> str:
        return f"RectangularParallelepiped: a={self.a} b={self.b} c={self.c}"
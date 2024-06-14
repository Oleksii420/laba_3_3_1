from Triangle import Triangle

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, l):
        super().__init__(a, b, c)
        self.l = l

    # def semiperimeter(self):
    #     return self.perimeter() / 2
    # # def perimeter(self):
    # #     return self.a + self.b + self.c

    def height(self):
        return self.l

    def volume(self):
        result = super().volume() * self.l
        if isinstance(result, complex):

            result_list = [round(result.real, 2), round(result.imag, 2)]
            nonComplexReslt = max(result_list)
            return nonComplexReslt
        else:

            return round(result, 2)

    def squareBase(self):
        return super().volume()

    def squareSurface(self):

        return self.a * self.l + self.b * self.l + self.c * self.l

    def __str__(self) -> str:
        return f"TriangularPrism: a={self.a} b={self.b} c={self.c} l={self.l}"
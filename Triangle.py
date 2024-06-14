from Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        my_list = [a, b, c]
        my_list.sort()
        a, b, c = my_list
        assert a + b > c
        self.a = a
        self.b = b
        self.c = c

    def semiperimeter(self):
        return self.perimeter() / 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        result = (self.semiperimeter() * (self.semiperimeter() - self.a) * (self.semiperimeter() - self.b) * (self.semiperimeter() - self.c)) ** 0.5
        return result

    def dimention(self):
        return 2

    def volume(self):
        return self.square()

    def __str__(self) -> str:
        return f"Triangle: a={self.a} b={self.b} c={self.c}"

if __name__ == "__main__":
    triangle = Triangle(3, 4, 5)
    print(triangle.height())
    print(triangle.perimetr())
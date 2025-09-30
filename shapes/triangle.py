import math
from .base import Shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть положительными числами")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Такого треугольника не существует")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
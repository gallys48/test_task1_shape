import math
from shapes import Circle, Triangle

def test_circle_area():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi)

def test_circle_invalid():
    try:
        Circle(0)
        assert False, "Должно выбрасывать ValueError"
    except ValueError:
        pass

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)

def test_triangle_invalid():
    try:
        Triangle(1, 2, 3)
        assert False, "Должно выбрасывать ValueError"
    except ValueError:
        pass

def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right() is True

def test_triangle_not_right():
    t = Triangle(2, 3, 4)
    assert t.is_right() is False
# Although shapes can be very different by nature, they can be sorted by the size of their area.
#
# Task:
#
# Create different shapes that can be part of a sortable list. The sort order is based on the size of their respective areas:
# The area of a Square is the square of its side
# The area of a Rectangle is width multiplied by height
# The area of a Triangle is base multiplied by height divided by 2
# The area of a Circle is the square of its radius multiplied by π
# The area of a CustomShape is given
#
# The default sort order of a list of shapes is ascending on area size:
# side = 1.1234
# radius = 1.1234
# base = 5
# height = 2
#
# # All classes must be subclasses of the Shape class
#
# shapes: List[Shape] = [Square(side), Circle(radius), Triangle(base, height)]
# shapes.sort()
# Use the correct π constant for your circle area calculations:
# math.pi
#
# SORTINGFUNDAMENTALSMATHEMATICSDESIGN PATTERNSARRAYSGEOMETRY
# Solution
from math import pi


class Shape:
    def __init__(self):
        self.area: float = 0.0

    def __lt__(self, x) -> bool:
        return self.area < x.area

    def __gt__(self, x) -> bool:
        return self.area > x.area

    def __eq__(self, x) -> bool:
        return self.area == x.area

    def __le__(self, x) -> bool:
        return self.area <= x.area

    def __ge__(self, x) -> bool:
        return self.area >= x.area

    def __ne__(self, x) -> bool:
        return self.area != x.area


class Square(Shape):
    def __init__(self, side: int):
        super().__init__()
        self.area = side ** 2


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.area = width * height


class Triangle(Shape):
    def __init__(self, base: int, height: int):
        super().__init__()
        self.area = (base * height) / 2


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.area = radius ** 2 * pi


class CustomShape(Shape):
    def __init__(self, area: float):
        super().__init__()
        self.area = area
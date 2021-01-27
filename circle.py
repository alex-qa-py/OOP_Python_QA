import math

from figure import Figure


class Circle(Figure):
    __name = "Circle"
    __angles = 0

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("parameter must be an integer or float")
        if radius <= 0:
            raise ValueError("parameter must be greater than zero")
        self.__radius = radius

    @classmethod
    def name(cls):
        return cls.__name

    @classmethod
    def angles(cls):
        return cls.__angles

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def add_area(self, figure):
        if not issubclass(figure.__class__, Figure):
            raise TypeError("Wrong class. Class must inherited from Figure")
        else:
            return figure.area() + self.area()

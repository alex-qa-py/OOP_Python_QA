import math

from figure import Figure


class Triangle(Figure):
    __name = "Triangle"
    __angles = 3

    def __init__(self, a_side_length, b_side_length, c_side_length):
        if not isinstance(a_side_length and b_side_length and c_side_length, (int, float)):
            raise TypeError("parameters must be integers or floats")
        if a_side_length <= 0 or b_side_length <= 0 or c_side_length <= 0:
            raise ValueError("parameters must be greater than zero")
        self.__a_side = a_side_length
        self.__b_side = b_side_length
        self.__c_side = c_side_length

    @classmethod
    def name(cls):
        return cls.__name

    @classmethod
    def angles(cls):
        return cls.__angles

    def area(self):
        half_perimeter = (self.__a_side + self.__b_side + self.__c_side) / 2
        return math.sqrt((half_perimeter * (half_perimeter - self.__a_side) * (half_perimeter - self.__b_side) * (
                half_perimeter - self.__c_side)))

    def perimeter(self):
        return self.__a_side + self.__b_side + self.__c_side

    def add_area(self, figure):
        if not issubclass(figure.__class__, Figure):
            raise TypeError("Wrong class. Class must inherited from Figure")
        else:
            return figure.area() + self.area()

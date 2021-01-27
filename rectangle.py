from figure import Figure


class Rectangle(Figure):
    __name = "Rectangle"
    __angles = 4

    def __init__(self, a_length, b_width):
        if not isinstance(a_length and b_width, (int, float)):
            raise TypeError("parameters must be integers or floats")
        if a_length <= 0 or b_width <= 0:
            raise ValueError("parameters must be greater than zero")
        self.__a_length = a_length
        self.__b_width = b_width

    @classmethod
    def name(cls):
        return cls.__name

    @classmethod
    def angles(cls):
        return cls.__angles

    def area(self):
        return self.__a_length * self.__b_width

    def perimeter(self):
        return (self.__a_length * self.__b_width) * 2

    def add_area(self, figure):
        if not issubclass(figure.__class__, Figure):
            raise TypeError("Wrong class. Class must inherited from Figure")
        else:
            return figure.area() + self.area()

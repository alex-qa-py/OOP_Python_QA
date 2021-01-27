from figure import Figure


class Square(Figure):
    __name = "Square"
    __angles = 4

    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("parameter must be an integer or float")
        if side_length <= 0:
            raise ValueError("parameter must be greater than zero")
        self.__side_length = side_length

    @classmethod
    def name(cls):
        return cls.__name

    @classmethod
    def angles(cls):
        return cls.__angles

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return self.__angles * self.__side_length

    def add_area(self, figure):
        if not issubclass(figure.__class__, Figure):
            raise TypeError("Wrong class. Class must inherited from Figure")
        else:
            return figure.area() + self.area()


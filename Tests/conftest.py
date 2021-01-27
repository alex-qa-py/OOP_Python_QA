import pytest

from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


@pytest.fixture(scope="session")
def create_square():
    return Square(3)


@pytest.fixture(scope="session")
def create_rectangle():
    return Rectangle(3, 4)


@pytest.fixture(scope="session")
def create_circle():
    return Circle(3)


@pytest.fixture(scope="session")
def create_triangle():
    return Triangle(3, 4, 4)

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def name(self):
        return NotImplemented

    @abstractmethod
    def area(self):
        return NotImplemented

    @abstractmethod
    def angles(self):
        return NotImplemented

    @abstractmethod
    def perimeter(self):
        return NotImplemented

    @abstractmethod
    def add_area(self, figure):
        return NotImplemented

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    __side = None

    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


square1 = Square(5)
print(square1.area())
print(square1.perimeter())
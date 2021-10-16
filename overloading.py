import math

class Circle:
    __radius = None

    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, other):
        return Circle(self.__radius + other.__radius)

    def __sub__(self, other):
        return Circle(self.__radius - other.__radius)

    def __str__(self):
        return "Circle Radius " + str(self.__radius)

circle_1 = Circle(10)
circle_2 = Circle(3)
#overloading addition operator
circle_3 = circle_1 + circle_2

#overloading subtraction operator
circle_4 = circle_1 - circle_2

print(circle_1.get_radius())
print(circle_2.get_radius())
print(circle_3.get_radius())
print(circle_4.get_radius())
print(circle_3.area())
print(str(circle_1))

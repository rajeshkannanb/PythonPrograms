#Define Base class with __init__, getter and setter methods.
class Polygon:
    __height = None
    __width = None

    def __init__(self):
        self.__height = 10
        self.__width = 10
        print('Default Width ', self.__width)
        print('Default height ', self.__height)

    def set_height(self, height):
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
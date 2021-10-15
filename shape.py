class Shape:
    __color = None

    def __init__(self):
        self.__color = 'white'
        print('Default color ', self.__color)

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color
from polygon import Polygon
from shape import Shape
#Inherit the class polygon, In class Triangle, the private members of polygon cannot be accessed.
#Multiple inheritance, inherit Shape class along with Polygon class.
class Triangle(Polygon, Shape):

    def __init__(self):
        #super().__init__()   #This statement will invoke __init__() method of first super class. i.e., Shape
        Polygon.__init__(self)
        Shape.__init__(self)
        self.set_height(40)
        self.set_width(5)

    def area(self):
        return self.get_height() * self.get_width() / 2



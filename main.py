from rectangle import Rectangle
from triangle import Triangle

rect = Rectangle()  #object creation
print('rectangle width', rect.get_width()) #Invoke the base class method
print('rectangle height', rect.get_height()) #Invoke the base class method
print('rectangle area', rect.area()) #Invoke sub class method
rect.set_color('red')
print(rect.get_color())

rect2 = Rectangle()
rect2.set_height(20) #Invoke the base class method
rect2.set_width(20) #Invoke the base class method
print(rect2.area()) #Invoke sub class method

tri = Triangle()
print(tri.get_height())
print(tri.get_width())
print(tri.area())
tri.set_color('blue')
print(tri.get_color())
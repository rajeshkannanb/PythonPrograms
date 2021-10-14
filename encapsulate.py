class Encapsulate:
    #declare private variables
    __speed = None
    __color = None

    #Init method for class
    def __init__(self):
        self.__speed = 100
        self.__color = "Grey"

    #public method to set the speed of car
    def set_speed(self, speed):
        self.__speed = speed

    #public method to set the color of car
    def set_color(self, color):
        self.__color = color

    #private method to get the speed of car
    def __get_speed(self):
        return self.__speed

    #private method to get the color of car
    def __get_color(self):
        return self.__color

    #public method to display properties of car
    def print_car_properties(self):
        print(self.__get_speed())
        print(self.__get_color())


#create object for class Encapsulate which will invoke the __init__ method.
honda = Encapsulate()
#honda.__speed = 200    //Invalid. Syntax is right. But the speed value will not be overriden.
honda.print_car_properties()

hyndai = Encapsulate()
hyndai.set_speed(200)
hyndai.print_car_properties()

ecoSport = Encapsulate()
ecoSport.set_speed(300)
ecoSport.set_color("Red")
#ecoSport.__get_speed()  //Invalid invocation since the method is private.
ecoSport.print_car_properties()

class Circle:
    def __init__(self,radius):
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_radius(self,new_radius):
        self.__radius = new_radius

radius = Circle(10)
print(radius.get_radius())

radius.set_radius(100)
print(radius.get_radius())

"print(radius.radius)"

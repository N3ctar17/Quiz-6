import math

class Shape:
    def get_area(self):
        raise NotImplementedError("get_area() method not implemented.")
    
    def set_width(self, width):
        raise NotImplementedError("set_width() method not implemented.")
    
    def set_height(self, height):
        raise  NotImplementedError("set_height() method not implemented.")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
    
    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
        
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height
        
class Polygon(Shape):
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def get_area(self):
        return (self.sides * self.length ** 2) / (4 * math.tan(math.pi / self.sides))
        
def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(4, 6)
    polygon = Polygon(6, 5)

    print("Area of Circle: ", circle.get_area())
    print("Area of Rectangle: ", rectangle.get_area())
    print("Area of Triangle: ", triangle.get_area())
    print("Area of Polygon: ", polygon.get_area())

if __name__ == "__main__":
    main()
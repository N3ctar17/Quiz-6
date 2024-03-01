from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def get_area(self):
        return self.side ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
def main():
    circle = Circle(3)
    square = Square(4)
    rectangle = Rectangle(3, 6)


    print("Area of Circle: ", circle.get_area())
    print("Area of Square ", square.get_area())
    print("Area of Rectangle ", rectangle.get_area())

if __name__ == "__main__":
    main()
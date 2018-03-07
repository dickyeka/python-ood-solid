
from abc import ABCMeta, abstractmethod

class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class AreaCalculator(object):

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area
        return total

def main():
    shapes = [Rectangle(1, 6), Rectangle(2, 3)]
    calculator = AreaCalculator(shapes)

    print ("The total area is: ", calculator.total_area)

if __name__ == '__main__':
    main()

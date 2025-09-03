'''
GRPA 3 - Shape and Square Classes - GRADED

Problem statement:
Implement a base class `Shape` with attributes name, area, and perimeter.  
Also implement a derived class `Square` that inherits from Shape and computes 
the area and perimeter of a square.  

Class Specifications:

1. class Shape:
    __init__(self, name):
        Initializes the shape with given name, sets area and perimeter as None.
    
    display(self):
        Prints the name, area, and perimeter of the shape.

2. class Square(Shape):
    __init__(self, side):
        Initializes the square with side length, computes its area and perimeter.
    
    compute_area(self):
        Computes the area of the square (side²).
    
    compute_perimeter(self):
        Computes the perimeter of the square (4 × side).
'''

# Solution

class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
        self.compute_area()
        self.compute_perimeter()

    def compute_area(self):
        self.area = self.side ** 2

    def compute_perimeter(self):
        self.perimeter = 4 * self.side


# Example usage
sq = Square(5)
sq.display()
# Output: Square has an area of 25 and perimeter of 20

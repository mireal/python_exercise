"""Day 13"""

"""
Question 47
Question
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle(self):
        circle = 2 * 3.14 * self.radius
        return round(circle)

# a = Circle(4)
# print(a.circle())

"""
Question 48
Question
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.
"""

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.widht = width

    def area(self):
        area = self.lenght * self.widht
        return area

# rect = Rectangle(4,5)
# print(rect.area())

"""
Question 49
Question
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints
To override a method in super class, we can define a method with the same name in the super class.
"""

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght = 0):
        Shape.__init__(self)
        self.lenght = lenght
    def area(self):
        return self.lenght * self.lenght

# square = Square(5)
# print(square.area())

"""
Question 50
Question
Please raise a RuntimeError exception.

Hints
UUse raise() to raise an exception.
"""

# raise RuntimeError("Error!")
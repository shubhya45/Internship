# Rectangle Class
# Private Attributes: __width and __height.

# Properties:

# width and height with getters and setters (no negatives).

# Method:

# area() returns the area of the rectangle.
class Rectangle:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.width = width   
        self.height = height 

    @property
    def width(self):
        return self.__width
    
    @property
    def height

    def area(self):
        return self.__width * self.__height

# Test the Rectangle class
rect = Rectangle(5, 10)
print("Width:", rect.width)
print("Height:", rect.height)
print("Area:", rect.area())

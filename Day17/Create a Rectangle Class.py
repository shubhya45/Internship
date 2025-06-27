# Create a Rectangle Class
# Attributes: length, width.

# Methods:

# area() — Returns the area of the rectangle.

# perimeter() — Returns the perimeter.

# Test it: Create a few instances and print their area and perimeter.

class Rectangle:
    # length=0
    # width=0
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length+self.width)
r1=Rectangle(120,60)
print("Area of rectangle is: ",r1.area())
print("perimeter of rectangle is:- ",r1.perimeter())  


r2=Rectangle(450,31)
print("Area of rectangle is: ",r2.area())
print("perimeter of rectangle is:- ",r2.perimeter())  
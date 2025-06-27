# Tasks on Encapsulation
# Task: Private Attribute and Method
# Instructions:

# Create a class Car.

# Add a private attribute __speed.

# Create a method accelerate(value) to increase the __speed.

# Create a method get_speed() to return the current __speed.

# Try accessing __speed directly (and understand why it doesn’t work).
class Car:
    def __init__(self):
        self.__speed=0
    def accelerate(self):
        self.__speed+=20
        
    

    def get_speed(self):
        return self.__speed

# Create an instance of Car
my_car = Car()
my_car.accelerate()
print(my_car.get_speed())


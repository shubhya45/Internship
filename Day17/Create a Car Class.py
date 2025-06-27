# Create a Car Class
# Attributes:

# brand (string), model (string), speed (initially 0).

# Methods:

# accelerate() — Increases speed by 10.

# brake() — Decreases speed by 5.

# display_speed() — Shows the current speed.

# Test it: Create a car object, call accelerate() and brake() a few times, and display the speed.

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#         self.speed=0
#     def accelerate(self):
#         self.speed+=10
#     def brake(self):
#         self.brake-=5
#     def display_speed(self):
#         print(f"Shows the current speed of {self.brand} and {self.model} is:- {self.speed} km/h")
# c1=Car("Toyota","shssj")
# print(f"{c1.brand} {c1.model}")
# c1.accelerate()
# c1.brake()    
# c1.display_speed()    
    
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
            self.speed -= 5
       
    def display_speed(self):
        print(f"The current speed of {self.brand} {self.model} is {self.speed} km/h.")

car=Car("Toyota", "Corolla")

print(f"Car: {car.brand} {car.model}")
car.display_speed()

car.accelerate()
car.display_speed()

car.accelerate()
car.display_speed()

car.brake()
car.display_speed()

car.brake()
car.display_speed()

     
# Task: 
# Create a parent class Vehicle with:

# An attribute brand.

# A method describe() that returns: "This is a vehicle."

# Create a child class Car that inherits from Vehicle and:

# Adds an attribute model.

# Overrides the describe() method to return: "This is a [brand] [model]."

# Test it:
# Create an object of Car and call its describe() method.
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def describe(self):
        return "This is vehicle"
class Car(Vehicle):
    def describe(self):
        return f"This is a {self.brand} model in {self.model} "
C1=Car("Innova",2024)
print(C1.describe())
    
        
# Create a Person class
# Add an _init_ method that takes name and age.

# Add a method called introduce() that prints:

# Hi, I am <name> and I am <age> years old.

# Test:
# Create an object (Person("Alice", 25)) and call introduce().

class Person:
    # name="Shubham"
    # age=19
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} year old")

p2=Person("Shubham",19)
p2.introduce()
        


        
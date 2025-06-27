# Task: Getters and Setters
# Instructions:

# Create a class Person.

# Add a private attribute __age.

# Create:

# A method set_age(value) that validates if the age is a positive number.

# A method get_age() to return the age.

# Try setting both valid and invalid ages.
class person:
    def __init__(self):
        self.__age=None
    
    def set_age(self,value):
        if value>0:
            self.__age=value
        else:
            print("Negative Age")
    
    def get_age(self):
        return self.__age

p=person()
print("Positive Number....")
p.set_age(20)
print("Your age is ",p.get_age())
print("Negative Number ")
p.set_age(-2)
if p.set_age==True:
    print("Your age is: ",p.get_age())
else:
    print("Invalid age")


    
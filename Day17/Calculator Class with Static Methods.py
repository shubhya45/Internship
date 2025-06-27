# Calculator Class with Static Methods
# Create a Calculator class:

# add(a, b) — Static method

# multiply(a, b) — Static method

# is_even(number) — Static method

# Test it: Call these methods without creating an object, like:

# Calculator.add(5, 3)  # Returns 8
class calculator:
    @staticmethod
    def add(a,b):
        return a+b 
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def is_even(number):
        return number%2==0
    
    
print(calculator.add(4,8))
print(calculator.multiply(4,5))
print(calculator.is_even(5))
    

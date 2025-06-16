# Part A: Arithmetic Practice
# 1.	Take two numbers from the user and perform:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# o	Floor Division
# o	Modulus
# o	Exponentiation
# Format your output nicely using f-strings.
# Example:
# print(f"Sum of {a} and {b} is {a+b}")

# all arithmatic operations 
A = int(input("Enter the value of a  : "))
B = int(input("Enter the value of B  : "))

# Addition
Sum = A + B 
print(f"Addition of {A} And {B} is : {Sum}")

# Substrction
Sub = A - B
print(f"Substraction of {A} And {B} is : {Sub}") 

# Multiplication
Mul = A * B 
print(f"Multiplication of {A} And {B} is : {Mul}")

# Division 
Div = A / B 
print(f"Division of {A} And {B} is : {Div}")

# Modulus
Mod = A % B 
print(f"Modulus of {A} And {B} is : {Mod}")

# Flow Division
Flowd = A // B
print(f"The flow division of {A} And {B} is : {Flowd}")

# Exponential value
expo = A ** B
print(f"The Exponential value of {A} And {B} is : {expo}")

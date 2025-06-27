# 🔹 Part C: Creating and Using a Custom Module
# 6.	Create a file math_utils.py with these functions:
# o	add(a, b) – returns the sum.
# o	multiply(a, b) – returns the product.
# o	is_even(n) – returns True if even.
# 7.	In a separate script (main.py), import math_utils and test all its functions.
# 8.	Modify math_utils.py:
# o	Add a greet() function that takes a name and returns a greeting.
# o	Import and test it in main.py.


def add(a,b):
    print(f"sum of {a} and {b} is : {a + b}")
    
def multiply(a,b):
    print(f"the product of {a} and {b} is : {a * b}")
    
def is_even(n):
    if n % 2 == 0:
        print(f"{n} is even number ..")
    else:
        print(f"{n} is odd numbeer .. ")
        
def greet(name):
    print(f"hello {name}")

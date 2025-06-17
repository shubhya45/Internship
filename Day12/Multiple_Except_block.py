# Multiple Except Blocks

# Input: take a number and a file name.

# Divide 100 by the number and open the file.

# Catch both ZeroDivisionError and FileNotFoundError.
try:
    num=int(input("Enter the number"))
    fileName=input("Enter the file name")

    d=100/num
    file=open(fileName,"r")
    
except ZeroDivisionError:
    print("Cannot divide number by 0")
except FileNotFoundError:
    print("file not found")

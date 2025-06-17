# Ask the user to input a number and a file name.

# Divide 100 by the number.

# If successful, try to open the given file in read mode.

# Use try, except, and else to structure the code.

try:
    num=int(input("Enter the number"))
    fileName=input("Enter the file name")

    d=100/num
    file=open("notes.txt","r")
    
except ZeroDivisionError:
    print("Cannot divide number by 0")
except FileNotFoundError:
    print("file not found")

else:
    print("Division",d)
    print("file found successfully")
file.close()
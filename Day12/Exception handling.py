a=int(input("Enter the number:- "))
b=int(input("Enter the second number:- "))

try:
    d=a/b
    print("Division",d)
except ZeroDivisionError:
    print("Canot divide number by 0")



# 5.	Ask the user to enter a number, and keep asking until they enter a number greater than 100


number = int(input("Enter a number: "))

while number <= 100:
    print("Number is less than 100")
    number = int(input("Enter a number: "))

print("Number greater than 100 entered :", number)

import random

choice ='y'

while choice!='n':
    print(random.randint(1,6))
    choice=input("Do you want to roll again(y/n): ")

print("Ended")
# Task 4: Dictionary and File Handling
# Instructions:

# Create a dictionary: prices = {"apple": 10, "banana": 5}

# Ask user for a fruit name and a filename.

# Try to print the price of the fruit and open the file.

# Catch KeyError and FileNotFoundError.

prices = {"apple": 10, "banana": 5}
try:
    fruitName=input("Enter the fruit name:- ")
    price=prices[fruitName]
    filename=("Enter the file name:- ")

    file=open(filename,"r")
    file.read()
    print("Enter the price of fruit",price)
    print("the file content",file)
    

except (KeyError,FileNotFoundError) as e:
    print("file not found")
    print(e)

    
   

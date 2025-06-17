# Task 3: List Access and Conversion
# Instructions:

# Create a list: data = [10, 20, 30]

# Ask the user for an index.

# Access that index and convert it to a float.

# Catch both IndexError and ValueError.
data = [10, 20, 30,"Shubham"]
try:
    Ind=int(input("Enter the Index"))
    v=data[Ind]
    f=float(v)
# except IndexError:
#     print("Incorrect index")
# except ValueError:
#     print("Value not converted")

except (IndexError,ValueError) as e:
    print(e)
